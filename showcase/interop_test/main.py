"""
Cross-Project Interoperability Demo
...
"""
print("DEBUG: Script Start")
import sys
import time
from pathlib import Path

# 添加路径以便导入各项目的 SDK
BASE_PATH = Path(r"C:\Users\Buxiaomaomaozi\Desktop\CONSOL")
sys.path.append(str(BASE_PATH / "examples" / "password_vault"))
sys.path.append(str(BASE_PATH / "showcase" / "01_todo_pro"))

try:
    from vault.sdk import VaultSDK
    # 手动定义 TodoSDK 避免导入 gui.py 时的副作用
    import requests
    class TodoSDK:
        def __init__(self, url="http://127.0.0.1:8001"):
            self.url = url
        def add(self, task):
            return requests.post(f"{self.url}/todos", json={"task": task}).json()
        def list(self):
            return requests.get(f"{self.url}/todos").json()
except Exception as e:
    print(f"❌ 导入失败: {e}")

def cross_test():
    print("🌉 开始跨项目互操作测试 (Cross-Project Interop)...")
    
    # 初始化两个项目的 SDK
    vault = VaultSDK("http://127.0.0.1:8000")
    todo = TodoSDK("http://127.0.0.1:8001")
    
    print("\n1️⃣ 访问 Password Vault 安全中心...")
    if vault.login("automated_user", "Aa123456"):
        print("✅ Vault: 成功获取安全 Token")
        
        # 存储并检索一个“任务指令”
        task_name = "Inter-Project Automation Task"
        vault.add_password("WorkflowBot", "system", task_name)
        
        # 检索刚才存入的指令
        secrets = vault.list_passwords()
        secure_task = [s['password'] for s in secrets if s['site_name'] == "WorkflowBot"][-1]
        print(f"✅ Vault: 成功检索到加密的任务指令: '{secure_task}'")
        
        print("\n2️⃣ 将 Vault 中的指令同步至 Todo Master Pro...")
        todo.add(f"Vault-Triggered: {secure_task}")
        
        # 验证 Todo 项目是否接收到
        tasks = todo.list()
        if any(secure_task in t['task'] for t in tasks):
            print("🎉 互操作性测试成功！两个独立项目已通过 SDK 完成协同通讯。")
        else:
            print("❌ Todo 项目未收到预期任务。")
    else:
        print("❌ Vault 登录失败，请确保 app.py(8000) 正在运行。")

if __name__ == "__main__":
    cross_test()
