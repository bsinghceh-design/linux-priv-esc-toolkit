import os
import subprocess

def get_system_info():
    info = {}

    # current user
    info["user"] = subprocess.getoutput("whoami")

    # id (uid, gid, groups)
    info["id"] = subprocess.getoutput("id")

    # kernel info
    info["kernel"] = subprocess.getoutput("uname -a")

    # OS release
    info["os_release"] = subprocess.getoutput("cat /etc/os-release")

    # PATH variable
    info["path"] = os.environ.get("PATH", "")

    return info

def print_system_info(info):
    print("[*] System Information")
    print("----------------------")
    for key, value in info.items():
        print(f"{key}: {value}")
