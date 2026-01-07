import requests
import base64
import os
from typing import Optional, List
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CognisSDK:
    def __init__(self, base_url: str = "http://127.0.0.1:8888", timeout: int = 5):
        self.base_url = base_url
        self.token: Optional[str] = None
        self.encryption_key: Optional[bytes] = None
        self.timeout = timeout

    def check_connection(self) -> bool:
        """检查与 API 服务器的连接是否正常"""
        try:
            response = requests.get(f"{self.base_url}/docs", timeout=self.timeout)
            return response.status_code in [200, 307, 404]  # API 存活即可
        except (requests.ConnectionError, requests.Timeout, requests.RequestException):
            return False

    def _derive_key(self, password: str, salt: bytes = b'cognis_static_salt'):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def register(self, username, password):
        """注册新用户"""
        try:
            payload = {"username": username, "hashed_password": password}
            response = requests.post(f"{self.base_url}/register", json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "error", "message": f"网络连接失败: {str(e)}"}

    def login(self, username, password):
        """登录并获取访问令牌"""
        try:
            response = requests.post(
                f"{self.base_url}/token", 
                data={"username": username, "password": password},
                timeout=self.timeout
            )
            if response.status_code == 200:
                self.token = response.json().get("access_token")
                # Crucial: Derive encryption key from password locally
                self.encryption_key = self._derive_key(password)
                return True
            return False
        except requests.RequestException:
            return False

    def add_secret(self, title: str, service_type: str, raw_content: str):
        """添加加密的密钥记录"""
        if not self.encryption_key or not self.token: 
            return None
        
        try:
            f = Fernet(self.encryption_key)
            encrypted_data = f.encrypt(raw_content.encode()).decode()
            
            headers = {"Authorization": f"Bearer {self.token}"}
            payload = {
                "title": title,
                "service_type": service_type,
                "encrypted_payload": encrypted_data
            }
            response = requests.post(
                f"{self.base_url}/records", 
                json=payload, 
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None

    def list_secrets(self) -> List[dict]:
        """列出所有密钥并解密内容"""
        if not self.token: 
            return []
        
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.base_url}/records", 
                headers=headers,
                timeout=self.timeout
            )
            if response.status_code != 200: 
                return []
            
            records = response.json()
            f = Fernet(self.encryption_key)
            
            decrypted_results = []
            for r in records:
                try:
                    r['payload'] = f.decrypt(r['encrypted_payload'].encode()).decode()
                except:
                    r['payload'] = "[Decryption Failed]"
                decrypted_results.append(r)
            return decrypted_results
        except requests.RequestException:
            return []

    def get_audit_logs(self):
        """获取审计日志"""
        if not self.token: 
            return []
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.base_url}/audit", 
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return []
