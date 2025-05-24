#Author: Sampad Mukherjee
#Description: A sample script to get the output of `sh ip interface brief`
from netmiko import ConnectHandler
router={
    "device_type" : "cisco_ios",
    "host" : "192.168.234.120",
    "username" : "admin",
    "password" : "admin"
}

net_connect = ConnectHandler(**router)
result = net_connect.send_command("sh ip int br")
print(result)
net_connect.disconnect()
