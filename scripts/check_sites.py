#!/usr/bin/env python3
import requests

def check_health(url):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code, r.elapsed.total_seconds()
    except Exception as e:
        return None, str(e)

def main():
    with open('../input/site_vips.txt') as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        status, info = check_health(url)
        if status:
            print(f"[+] {url} is UP (Status: {status}, Response Time: {info:.2f}s)")
        else:
            print(f"[!] {url} is DOWN or Unreachable ({info})")

if __name__ == "__main__":
    main()
