from modules import system_info, suid_sgid, permissions, cron_jobs, sudo_check, kernel_check

def main():
    report_lines = []

    # 1. SYSTEM INFORMATION
    info = system_info.get_system_info()
    system_info.print_system_info(info)
    report_lines.append("[SYSTEM INFO]")
    for k, v in info.items():
        report_lines.append(f"{k}: {v}")
    report_lines.append("")

    # 2. SUID / SGID SCAN
    suid_results = suid_sgid.scan_suid_sgid()
    suid_sgid.print_suid_sgid(suid_results)
    report_lines.append("[SUID_SGID]")
    for r in suid_results:
        report_lines.append(f"{r['path']} ({r['binary']}) Risk: {r['risk']}")
    report_lines.append("")

    # 3. PERMISSIONS SCAN
    ww_files = permissions.scan_world_writable()
    critical_info = permissions.check_critical_files()
    permissions.print_permissions(ww_files, critical_info)
    report_lines.append("[PERMISSIONS_CRITICAL]")
    report_lines.append(critical_info)
    report_lines.append("")
    report_lines.append("[PERMISSIONS_WORLD_WRITABLE]")
    for line in ww_files[:200]:
        report_lines.append(line)
    report_lines.append("")

    # 4. CRON SCAN
    cron_info = cron_jobs.scan_cron()
    cron_jobs.print_cron(cron_info)
    report_lines.append("[CRON]")
    report_lines.append(cron_info)
    report_lines.append("")

    # 5. SUDO CHECK
    sudo_info = sudo_check.check_sudo()
    sudo_check.print_sudo(sudo_info)
    report_lines.append("[SUDO]")
    report_lines.append(sudo_info)
    report_lines.append("")

    # 6. KERNEL CHECK
    kernel_info = kernel_check.check_kernel()
    kernel_check.print_kernel(kernel_info)
    report_lines.append("[KERNEL]")
    report_lines.append(kernel_info)
    report_lines.append("")

    # SAVE REPORT
    with open("reports/report_latest.txt", "w") as f:
        f.write("\n".join(report_lines))

    print("\n[+] Report saved to reports/report_latest.txt")

if __name__ == "__main__":
    main()
