### Basic Level Networking Programs
#### Pinging a Host
```bash
import subprocess

def ping(host):
    try:
        output = subprocess.check_output(["ping", "-c", "4", host])
        print(output.decode())
    except subprocess.CalledProcessError:
        print(f"Failed to ping {host}")

if __name__ == "__main__":
    host = input("Enter host to ping (e.g., google.com): ")
    ping(host)
```
#### Validating an IP
```bash
import ipaddress

def validate_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        print(f"{ip} is a valid IPv{ip.version} address.")
    except ValueError:
        print(f"{ip_str} is not a valid IP address.")

if __name__ == "__main__":
    ip_input = input("Enter an IP address: ")
    validate_ip(ip_input)
```
#### Validating MAC Address
```bash
import re

def normalize_mac(mac):
    mac = re.sub(r'[^0-9A-Fa-f]', '', mac).upper()
    if len(mac) != 12:
        return None
    return ":".join(mac[i:i+2] for i in range(0, 12, 2))

if __name__ == "__main__":
    mac_input = input("Enter a MAC address: ")
    normalized = normalize_mac(mac_input)
    if normalized:
        print(f"Normalized MAC: {normalized}")
    else:
        print("Invalid MAC address.")
```
#### Resolving hostname
```bash
import socket

def resolve_hostname(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"{hostname} resolves to {ip}")
    except socket.gaierror:
        print(f"Failed to resolve {hostname}")

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., google.com): ")
    resolve_hostname(domain)
```

### Socket Command

>🔧 socket.socket(...)
This is how you create a new socket object. Think of a socket as a “virtual wire” for sending/receiving data between two machines on a network.
📡 socket.AF_INET
This tells Python you want to use IPv4 addresses (like 192.168.1.1).
AF_INET = Address Family: IPv4
(If you wanted IPv6, you would use AF_INET6.)
📬 socket.SOCK_STREAM
This specifies the type of socket — in this case, a stream socket, which is used for TCP connections.
SOCK_STREAM = TCP
(For UDP, you’d use SOCK_DGRAM instead.)

```bash
import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is open.")
        except socket.error:
            print(f"Couldn't connect to {host}")
            break

if __name__ == "__main__":
    target = input("Enter IP or hostname: ")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]
    scan_ports(target, common_ports)
```



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
