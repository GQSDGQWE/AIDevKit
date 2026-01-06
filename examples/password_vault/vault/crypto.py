"""
Local Password Vault - Cryptography Module
处理密码哈希、数据加密和 JWT 令牌。

PLAN:
1. 使用 bcrypt 进行主密码哈希验证。
2. 使用 cryptography.fernet 进行对称加密。
3. 提供生成密钥和加密/解密文本的方法。
4. 包含 JWT 生成逻辑。

EXECUTE:
"""

import bcrypt
import jwt
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from typing import Optional

SECRET_KEY = "local_vault_system_secret_key" # 建议从环境变量读取
ALGORITHM = "HS256"

class CryptoManager:
    """加密与安全管理器"""

    @staticmethod
    def hash_password(password: str) -> str:
        """哈希主密码"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """校验主密码"""
        return bcrypt.checkpw(password.encode(), hashed.encode())

    @staticmethod
    def encrypt_data(data: str, key: str) -> str:
        """使用 Fernet 加密敏感数据"""
        f = Fernet(key.encode())
        return f.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt_data(token: str, key: str) -> str:
        """解密敏感数据"""
        f = Fernet(key.encode())
        return f.decrypt(token.encode()).decode()

    @staticmethod
    def generate_encryption_key() -> str:
        """生成全新的 Fernet 密钥"""
        return Fernet.generate_key().decode()

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """生成登录令牌"""
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 自测脚本
if __name__ == "__main__":
    print("🧪 测试加密模块...")
    mgr = CryptoManager()
    
    # 1. 密码哈希测试
    pwd = "master_password"
    hashed = mgr.hash_password(pwd)
    assert mgr.verify_password(pwd, hashed) is True
    print("✅ 密码哈希验证通过")
    
    # 2. 加解密测试
    key = mgr.generate_encryption_key()
    secret = "my_secret_password_123"
    encrypted = mgr.encrypt_data(secret, key)
    decrypted = mgr.decrypt_data(encrypted, key)
    assert secret == decrypted
    print("✅ 数据加解密验证通过")
    
    # 3. JWT 测试
    token = mgr.create_access_token({"sub": "user1"})
    print(f"✅ JWT 生成成功: {token[:20]}...")
