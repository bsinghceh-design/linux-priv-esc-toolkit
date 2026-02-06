import subprocess

def check_kernel():
    print("\n[*] Checking kernel version...")
    kernel = subprocess.getoutput("uname -r")
    msg_lines = []
    msg_lines.append(f"Kernel version: {kernel}")
    msg_lines.append("Tip: Search online for known privilege escalation CVEs for this kernel,")
    msg_lines.append("for example: \"Linux kernel " + kernel + " privilege escalation\".")
    return "\n".join(msg_lines)

def print_kernel(info):
    print("[*] Kernel Information:")
    print("-----------------------")
    print(info)
