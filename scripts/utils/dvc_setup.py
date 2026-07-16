import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def initialize_dvc():
    # Check if .dvc already exists
    if os.path.exists(".dvc"):
        print("DVC is already initialized.")
        return True

    print("Initializing DVC...")
    # Resolve local virtual env dvc path if possible
    dvc_bin = "dvc"
    venv_bin_dir = os.path.dirname(sys.executable)
    local_dvc = os.path.join(venv_bin_dir, "dvc.exe" if os.name == "nt" else "dvc")
    if os.path.exists(local_dvc):
        dvc_bin = local_dvc

    # Initialize DVC without sending anonymous stats
    success = run_cmd([dvc_bin, "init", "--no-scm"])
    if not success:
        # Fallback to standard init
        success = run_cmd([dvc_bin, "init"])
    
    if success:
        # Disable analytics
        run_cmd([dvc_bin, "config", "core.analytics", "false"])
        print("DVC successfully initialized.")
        
        # Add basic DVC gitignore tracking config if needed
        # and configure local remote as placeholder
        os.makedirs("data/raw", exist_ok=True)
        os.makedirs("data/annotated", exist_ok=True)
        os.makedirs("data/gold", exist_ok=True)
        
        # Configure a local default storage bucket for data
        run_cmd([dvc_bin, "remote", "add", "-d", "local_storage", ".dvc/tmp/local_storage"])
        print("Local default DVC storage remote configured.")
    return success

if __name__ == "__main__":
    if not initialize_dvc():
        sys.exit(1)
