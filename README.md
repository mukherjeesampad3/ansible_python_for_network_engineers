# 🔧 ansible_python_for_network_engineers

A practical repository designed to help **network engineers** automate and manage network infrastructure using **Ansible** and **Python**.  
This project combines real-world examples, playbooks, and scripts that demonstrate how to integrate Python automation with Ansible for:

- Network operations
- Configuration management
- Device provisioning

---

## 📂 Project Features

- Ansible playbooks for automating device configurations
- Python scripts to enhance and extend Ansible's capabilities
- Integration examples with various network platforms
- Practical troubleshooting and error-handling tips

---

## ⚠️ Common SSH Issue & Fix

When connecting to legacy network devices, you may encounter the following error:

Unable to negotiate with 123.123.123.123 port 22: no matching key exchange method found.
Their offer: diffie-hellman-group1-sha1



### ✅ Solution

You can resolve this by explicitly specifying compatible key exchange and host key algorithms in your SSH configuration.

Add the following lines to your SSH configuration file (`~/.ssh/config`):

Host 123.123.123.123
KexAlgorithms +diffie-hellman-group1-sha1,diffie-hellman-group14-sha1
HostkeyAlgorithms ssh-dss,ssh-rsa


> 💡 Tip: Replace `123.123.123.123` with your actual device IP address.

---

## 📌 Requirements

- Python 3.x
- Ansible 2.9+
- Paramiko or Netmiko (depending on playbook/scripts)
- SSH access to network devices

---

## 🚀 Getting Started

Clone the repo:

```bash
git clone [https://github.com/your-username/ansible_python_for_network_engineers.git](https://github.com/mukherjeesampad3/ansible_python_for_network_engineers.git)
cd ansible_python_for_network_engineers
