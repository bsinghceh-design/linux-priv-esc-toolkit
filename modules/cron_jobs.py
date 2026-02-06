import subprocess

CRON_COMMANDS = [
    "crontab -l",
    "cat /etc/crontab",
    "ls -la /etc/cron.hourly /etc/cron.daily /etc/cron.weekly /etc/cron.monthly 2>/dev/null",
    "ls -la /etc/cron.d 2>/dev/null",
    "ls -la /var/spool/cron /var/spool/cron/crontabs 2>/dev/null"
]

def scan_cron():
    print("\n[*] Scanning cron jobs and cron directories...")
    all_output = []

    for cmd in CRON_COMMANDS:
        all_output.append(f"\n----- {cmd} -----\n")
        all_output.append(subprocess.getoutput(cmd))

    return "\n".join(all_output)

def print_cron(info):
    print("[*] Cron Information:")
    print("---------------------")
    print(info)
