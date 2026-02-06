import subprocess

def check_sudo():
    print("\n[*] Checking sudo permissions (you may be asked for password)...")
    output = subprocess.getoutput("sudo -l 2>/dev/null")
    if not output.strip():
        output = "No sudo permissions found or sudo -l not allowed."
    return output

def print_sudo(info):
    print("[*] Sudo Information:")
    print("---------------------")
    print(info)


