#Author: Sampad Mukherjee
#Description: This python script helps to set the dhcp rule for the router

from netmiko import ConnectHandler
router={
    "device_type" : "cisco_ios",
    "host" : "192.168.234.120",
    "username" : "admin",
    "password" : "admin",
    "port" : 22,
    "secret" : "admin"
}

net_connect = ConnectHandler(**router)
# Entering into enable mode
net_connect.enable()
net_connect.send_config_set([
    "ip dhcp pool Adminitrative-Team",
    "default-router 192.168.234.120",
    "network 192.168.234.0 255.255.255.0",
    "ip dhcp excluded-address 192.168.234.138 192.168.234.145"
])
#Write configuration to memory
net_connect.save_config()
net_connect.disconnect()
