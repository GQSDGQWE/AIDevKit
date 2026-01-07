print("Hello from Interop Test")
import requests
import sys
from pathlib import Path

# Manual SDK logic to be 100% sure
class VaultSDK:
    def __init__(self, url): self.url = url
    def login(self, u, p):
        r = requests.post(f"{self.url}/login", json={"username":u, "password":p})
        self.tk = r.json().get("access_token") if r.status_code==200 else None
        return self.tk is not None
    def add(self, s, u, p):
        return requests.post(f"{self.url}/passwords", json={"site_name":s, "site_username":u, "password":p}, headers={"Authorization": f"Bearer {self.tk}"}).status_code==200
    def list(self):
        return requests.get(f"{self.url}/passwords", headers={"Authorization": f"Bearer {self.tk}"}).json()

class TodoSDK:
    def __init__(self, url): self.url = url
    def add(self, t): return requests.post(f"{self.url}/todos", json={"task": t})
    def list(self): return requests.get(f"{self.url}/todos").json()

print("Connecting to Vault...")
v = VaultSDK("http://127.0.0.1:8000")
t = TodoSDK("http://127.0.0.1:8010")

if v.login("automated_user", "Aa123456"):
    print("[SUCCESS] Vault Logged In")
    v.add("Interop", "admin", "TargetAction_001")
    cmd = v.list()[-1]['password']
    print(f"[SUCCESS] Retrieved Cmd: {cmd}")
    t.add(f"Vault_Action: {cmd}")
    print("[SUCCESS] Todo Task Added")
    print(f"Current Todos: {t.list()}")
else:
    print("[ERROR] Vault Login Failed")
    requests.post("http://127.0.0.1:8000/register", json={"username":"automated_user", "password":"Aa123456"})
    if v.login("automated_user", "Aa123456"):
        print("[SUCCESS] Vault Registered & Logged In")
