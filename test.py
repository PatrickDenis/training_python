from netmiko import Netmiko
from getpass import getpass

csr1 = "10.100.100.3"
csr2 = "10.100.100.5"
csr3 = "10.100.100.1"

devices = [csr1, csr2, csr3]

dict1 = { 'host': "10.100.100.3", 'username': 'admin', 'password': 'cisco', 'device_type': 'cisco_ios', 'secret': 'cisco' }

for device in dict1:
    net_conn = Netmiko(**device)
    net_conn.enable()
    print(net_conn.find_prompt())
    
    print("--------------------------------------")
    print(net_conn.send_command("show ip arp"))
    print("--------------------------------------")
    

