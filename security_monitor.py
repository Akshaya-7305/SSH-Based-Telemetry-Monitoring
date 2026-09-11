blocked_ips = set()
failed_attempts = {}

def check_login(ip, success):
    if success:
        failed_attempts[ip] = 0
        return

    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    print(f"Failed login from {ip}")

    if failed_attempts[ip] >= 5:
        blocked_ips.add(ip)
        print(f"Blocked IP: {ip}")