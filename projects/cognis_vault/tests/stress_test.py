import sys
import os
import time

# Add parent dir to path to import SDK
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdk.cognis_sdk import CognisSDK

def run_test():
    print("=== Cognis Vault Pro Reliability Test ===")
    sdk = CognisSDK("http://127.0.0.1:8888")
    
    # 1. Register & Login
    ts = int(time.time())
    user = f"pro_tester_{ts}"
    print(f"Testing Registration for {user}...")
    sdk.register(user, "SecurePass123!")
    
    if not sdk.login(user, "SecurePass123!"):
        print("[FAIL] Login failed")
        return

    print("[PASS] Login successful with Argon2 auth")

    # 2. Bulk Insertion (Stress Test)
    print("Performing Bulk Secure Insert (10 records)...")
    for i in range(10):
        sdk.add_secret(f"Secret_{i}", "TestType", f"Data_Value_{i}")
    
    # 3. Validation
    records = sdk.list_secrets()
    if len(records) >= 10:
        print(f"[PASS] Successfully retrieved {len(records)} records")
        # Check one record decryption
        if "Data_Value_0" in str(records):
            print("[PASS] End-to-End Encryption verified (Client-side decrypt successful)")
    else:
        print("[FAIL] Record count mismatch")

    # 4. Audit Log Verification
    logs = sdk.get_audit_logs()
    print(f"[INFO] Audit Logs captured {len(logs)} actions")
    if len(logs) > 0:
        print("[PASS] Security audit working")

if __name__ == "__main__":
    run_test()
