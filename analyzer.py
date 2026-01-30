def read_logs():
    with open("windows_sample.log", "r") as file:
        return file.readlines()

def extract_ip(line):
    parts = line.strip().split()
    for part in parts:
        if "IP=" in part:
            return part.split("=")[1]
    return None

def is_failed_login(line):
    return "Failed login" in line

def is_error(line):
    return "ERROR" in line

def main():
    logs = read_logs()

    ip_count = {}
    failed_login_count = 0
    error_count = 0

    for log in logs:
        ip = extract_ip(log)

        if ip:
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

        if is_failed_login(log):
            failed_login_count += 1

        if is_error(log):
            error_count += 1

    print("\n--- ACTIVITY SUMMARY ---")
    print("Total log entries:", len(logs))
    print("Total failed logins:", failed_login_count)
    print("Total error events:", error_count)

    print("\n--- IP ACTIVITY COUNT ---")
    for ip, count in ip_count.items():
        print(ip, "->", count, "events")

    print("\n--- SUSPICIOUS IPs (more than 3 events) ---")
    for ip, count in ip_count.items():
        if count > 3:
            print("⚠️ Suspicious IP:", ip, "Events:", count)

if __name__ == "__main__":
    main()
