import subprocess
import time
import sys
import os
import signal

def main():
    print("--- Cognis Vault Pro System Bootstrap ---")
    
    # Robust path logic
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(base_dir) # The 'projects' folder
    workspace_root = os.path.dirname(root_dir) # The root folder
    
    py_path = sys.executable
    
    # 1. Start API Server in background
    print("[1/2] Launching Backend Secure Service (Port 8888)...")
    env = os.environ.copy()
    env["PYTHONPATH"] = workspace_root
    
    api_process = subprocess.Popen(
        [py_path, "-m", "projects.cognis_vault.api.main"],
        cwd=workspace_root,
        env=env
    )
    
    time.sleep(3) # Wait for server to initialize DB
    
    # 2. Start GUI
    print("[2/2] Launching Professional UI...")
    try:
        gui_process = subprocess.run(
            [py_path, "-m", "projects.cognis_vault.gui.main_window"],
            cwd=workspace_root,
            env=env
        )
    except KeyboardInterrupt:
        pass
    finally:
        print("\nShutting down Secure Service...")
        api_process.terminate()
        print("System cleanup complete.")

if __name__ == "__main__":
    main()
