import time
from datetime import datetime as dt

# Path to the hosts file (Windows/Linux/Mac)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows
# hosts_path = "/etc/hosts"  # For Linux or macOS (needs sudo)

redirect = "127.0.0.1"

# List of websites to block
website_list = [
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com"
]

# Time range for blocking (e.g., 9 AM to 5 PM)
block_start = 9
block_end = 17

while True:
    current_hour = dt.now().hour
    if block_start <= current_hour < block_end:
        print("Blocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"{redirect} {website}\n")
    else:
        print("Unblocking websites...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10)  # Checks every 10 seconds
    
