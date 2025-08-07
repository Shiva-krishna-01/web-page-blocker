import time
from datetime import datetime as dt

# Path to the hosts file (varies by OS)
HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"  # macOS/Linux
# HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"  # Windows

REDIRECT = "127.0.0.1"
WEBSITES = ["www.youtube.com"]

# Working hours (e.g., block from 9am to 5pm)
START_HOUR = 9
END_HOUR = 11

def block_websites():
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for website in WEBSITES:
            if website not in content:
                file.write(f"{REDIRECT} {website}\n")

def unblock_websites():
    with open(HOSTS_PATH, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in WEBSITES):
                file.write(line)
        file.truncate()

def main():
    while True:
        now = dt.now()
        if START_HOUR <= now.hour < END_HOUR:
            print("Work hours... Blocking websites")
            block_websites()
        else:
            print("Off hours... Unblocking websites")
            unblock_websites()
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()
