# Linux Privilege Escalation Toolkit

A comprehensive security assessment tool for identifying privilege escalation vectors on Linux systems.

## Features

- **System Information Gathering** - Kernel version, OS, user/group info
- **SUID/SGID Scanning** - Detects dangerous SUID/SGID binaries
- **Permission Analysis** - Identifies world-writable files and critical file permissions
- **Cron Job Enumeration** - Lists user and system cron jobs
- **Sudo Privileges Check** - Analyzes sudo configuration (sudoers)
- **Kernel Vulnerability Detection** - Identifies kernel exploits applicable to the system

## Installation

```bash
git clone https://github.com/bsinghceh-design/linux-priv-esc-toolkit.git
cd linux-priv-esc-toolkit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Output is saved to: `reports/report_latest.txt`

## Requirements

- Python 3.6+
- Linux/Unix system with sudo privileges for full functionality
- See `requirements.txt` for dependencies

## Module Descriptions

| Module | Purpose |
|--------|----------|
| `system_info.py` | Gather system information |
| `suid_sgid.py` | Scan for SUID/SGID vulnerabilities |
| `permissions.py` | Check file permissions and ownership |
| `sudo_check.py` | Analyze sudo configuration |
| `cron_jobs.py` | Enumerate cron jobs |
| `kernel_check.py` | Detect kernel vulnerabilities |

## Output

Generated reports are saved in the `reports/` directory with timestamps and detailed findings.

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is for educational purposes only. Use responsibly on systems you own or have explicit permission to test.
