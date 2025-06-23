# IP and MAC Address Parser

This repository contains two Python scripts designed for processing and analyzing IP and MAC addresses from input text files:

- **`ip_parser.py`** – Classifies and analyzes IP addresses (IPv4 and IPv6).
- **`mac_parser.py`** – Normalizes and analyzes MAC addresses.

---

## 📄 ip_parser.py

### Description
This script reads IP addresses from a file (`ips.txt`), validates them, determines their version (IPv4 or IPv6), identifies duplicates, and summarizes the results.

### Usage
```bash
python ip_parser.py
```

### Collections
```bash
from collections import Counter
ips = ['192.168.1.1', '10.0.0.1', '192.168.1.1', '10.0.0.1', '192.168.1.2']
ip_counts = Counter(ips)
print(ip_counts)
```
**Output**
```bash
Counter({'192.168.1.1': 2, '10.0.0.1': 2, '192.168.1.2': 1})
```
### Parse IP Address
```bash
import ipaddress
from collections import Counter

def load_ips(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def classify_ips(ip_list):
    ipv4, ipv6 = 0, 0
    for ip in ip_list:
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.version == 4:
                ipv4 += 1
            else:
                ipv6 += 1
        except ValueError:
            print(f"Invalid IP address skipped: {ip}")
    return ipv4, ipv6

def find_duplicates(ip_list):
    counter = Counter(ip_list)
    return [ip for ip, count in counter.items() if count > 1]

def main():
    ip_list = load_ips("ips.txt")
    total_ips = len(ip_list)
    unique_ips = set(ip_list)
    ipv4_count, ipv6_count = classify_ips(ip_list)
    duplicates = find_duplicates(ip_list)

    print(f"Total IP addresses: {total_ips}")
    print(f"Unique IP addresses: {len(unique_ips)}")
    print(f"IPv4 addresses: {ipv4_count}")
    print(f"IPv6 addresses: {ipv6_count}")

    if duplicates:
        print("Duplicate IPs:")
        for dup in duplicates:
            print(f" - {dup}")
    else:
        print("No duplicate IPs found.")

if __name__ == "__main__":
    main()
```

### Parse MACs
```bash
import re
from collections import Counter

def normalize_mac(mac):
    # Remove separators and convert to uppercase
    mac = re.sub(r'[^0-9A-Fa-f]', '', mac).upper()
    if len(mac) != 12:
        return None
    # Format as colon-separated: 00:1A:2B:3C:4D:5E
    return ":".join(mac[i:i+2] for i in range(0, 12, 2))

def load_and_clean_macs(filename):
    normalized = []
    with open(filename) as f:
        for line in f:
            mac = line.strip()
            if not mac:
                continue
            norm_mac = normalize_mac(mac)
            if norm_mac:
                normalized.append(norm_mac)
            else:
                print(f"Invalid MAC skipped: {mac}")
    return normalized

def find_duplicates(mac_list):
    counter = Counter(mac_list)
    return [mac for mac, count in counter.items() if count > 1]

def main():
    mac_list = load_and_clean_macs("macs.txt")
    total = len(mac_list)
    unique = set(mac_list)
    duplicates = find_duplicates(mac_list)

    print(f"Total MAC addresses: {total}")
    print(f"Unique MAC addresses: {len(unique)}")

    if duplicates:
        print("Duplicate MACs:")
        for mac in duplicates:
            print(f" - {mac}")
    else:
        print("No duplicate MACs found.")

if __name__ == "__main__":
    main()
```
