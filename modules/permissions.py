import subprocess

def scan_world_writable():
    print("\n[*] Scanning for world-writable files (this may take some time)...")
    cmd = "find / -writable -type f 2>/dev/null"
    output = subprocess.getoutput(cmd)
    files = output.splitlines()
    return files

def check_critical_files():
    print("\n[*] Checking permissions of critical files...")
    cmd = "ls -la /etc/passwd /etc/shadow 2>/dev/null"
    output = subprocess.getoutput(cmd)
    return output

def print_permissions(ww_files, critical_info):
    print("[*] Critical Files:")
    print("-------------------")
    print(critical_info)

    print("\n[*] Some world-writable files (first 30 shown):")
    print("---------------------------------------------")
    for line in ww_files[:30]:
        print(line)
    if len(ww_files) > 30:
        print(f"... and {len(ww_files)-30} more entries (see report file).")
