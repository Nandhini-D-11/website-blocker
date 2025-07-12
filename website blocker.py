from datetime import datetime

# Simulated hosts file as a list (instead of editing the real file)
hosts_file_simulated = []

# Redirect IP (used in real hosts file)
redirect_ip = "127.0.0.1"

# User enters websites to block
print(" Enter websites to block (comma-separated, e.g., facebook.com,youtube.com):")
input_websites = input()
websites = [site.strip() for site in input_websites.split(",")]

# Simulated blocking hours (can be changed)
block_start = 9   # 9 AM
block_end = 17    # 5 PM

# Get current hour (24-hour format)
current_hour = datetime.now().hour
print(f"\n Current Hour: {current_hour}:00")

# Apply blocking if in working hours
if block_start <= current_hour < block_end:
    print("\n Blocking websites during working hours...")
    for site in websites:
        entry = f"{redirect_ip} {site}"
        if entry not in hosts_file_simulated:
            hosts_file_simulated.append(entry)
            print(f"blocked: {site}")
        else:
            print(f"Already blocked: {site}")
else:
    print("\nIt's outside working hours. No blocking applied.")

# Display final simulated hosts file
print("\n Simulated Hosts File Content:")
if hosts_file_simulated:
    for line in hosts_file_simulated:
        print(line)
else:
    print("No entries added. Hosts file is clean.")
