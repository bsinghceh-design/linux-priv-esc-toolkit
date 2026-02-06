import subprocess

DANGEROUS_BINARIES = ["vim", "find", "perl", "python", "awk", "nmap", "less", "bash"]

def scan_suid_sgid():
    print("\n[*] Scanning for SUID/SGID binaries in common paths...")
    paths = ["/bin", "/sbin", "/usr", "/home", "/opt"]
    results = []

    for base in paths:
        cmd = f"find {base} -perm -4000 -o -perm -2000 2>/dev/null"
        output = subprocess.getoutput(cmd)
        for line in output.splitlines():
            path = line.strip()
            if not path:
                continue
            binary_name = path.split('/')[-1]
            risk = 'Low'
            if binary_name in DANGEROUS_BINARIES:
                risk = 'High'
            results.append({'path': path, 'binary': binary_name, 'risk': risk})

    return results

def print_suid_sgid(results):
    print("[*] SUID/SGID Binaries Found (limited paths):")
    print("-------------------------------------------")
    for r in results[:30]:
        print(f"{r['path']}  ({r['binary']})  Risk: {r['risk']}")
    if len(results) > 30:
        print(f"... and {len(results)-30} more entries (see report file).")
