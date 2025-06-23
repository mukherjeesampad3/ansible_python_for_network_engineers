
# 🐍 Python Essentials for Network Engineers — Code Snippets

---

## ✅ **Variables and Data Types**

```python
# Declaring variables
hostname = "router01"
interfaces = 24
is_active = True
temperature = 37.5

# Type conversion
port_str = str(interfaces)

# String formatting
print(f"Device {hostname} has {interfaces} interfaces. Status: {'Up' if is_active else 'Down'}")
```

---

## ✅ **Lists and Dictionaries**

```python
# List of IP addresses
ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]

# Looping through list
for ip in ip_list:
    print(f"Pinging {ip}...")

# Dictionary of devices
devices = {
    "router1": {"ip": "192.168.1.1", "status": "up"},
    "switch1": {"ip": "10.0.0.2", "status": "down"}
}

# Accessing nested dictionary
for device, info in devices.items():
    print(f"{device} ({info['ip']}) is {info['status']}")
```

---

## ✅ **Conditional Logic & Loops**

```python
# Conditional example
status = "down"
if status == "up":
    print("Device is operational")
elif status == "down":
    print("Device is unreachable")
else:
    print("Unknown status")

# Loop with control statements
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Stop at 7
    print(f"Port {i}")
```

---

## ✅ **Functions & Modules**

```python
# Function definition
def check_status(ip):
    return f"Ping {ip} successful"  # Simulated ping response

# Calling a function
print(check_status("192.168.1.1"))

# Importing a standard module
import os

# Using a module
print(os.name)  # 'posix' or 'nt' depending on OS
```

---

## ✅ **File I/O**

```python
# Reading a file
with open("devices.txt", "r") as file:
    for line in file:
        print(f"Device: {line.strip()}")

# Writing to a file
with open("results.txt", "w") as file:
    file.write("Scan complete.
")

# Working with paths
from pathlib import Path
config_path = Path("configs/router01.conf")
print(config_path.resolve())
```

---

## ✅ **Exception Handling**

```python
try:
    ip = input("Enter IP: ")
    if not ip:
        raise ValueError("IP cannot be empty")
    print(f"Pinging {ip}...")
except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Operation completed successfully.")
finally:
    print("Cleanup done.")
```

---

## ✅ **CLI Arguments with `argparse`**

```python
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description="Ping network devices")
parser.add_argument("ip", help="IP address of the device")
parser.add_argument("--count", type=int, default=4, help="Number of ping attempts")

args = parser.parse_args()

# Simulated ping command
print(f"Pinging {args.ip} {args.count} times...")
```

---

## 🛠️ **Lab Ready Snippet Starters**

### 📝 Lab 1: Parse and summarize IPs from a file

```python
with open("ip_list.txt") as f:
    ips = [line.strip() for line in f if line.strip()]
print(f"Total IPs found: {len(ips)}")
```

### 🔁 Lab 2: Automate CLI Tasks

```python
commands = ["show ip int brief", "show version", "show running-config"]
for cmd in commands:
    print(f"Executing: {cmd}")
    # Simulate sending command to device
```

### 📂 Lab 3: CLI Tool for Config Summary

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("config_file", help="Path to config file")
parser.add_argument("devices_file", help="Path to device list")

args = parser.parse_args()

print(f"Parsing config from {args.config_file}")
print(f"Devices listed in {args.devices_file}")
```
