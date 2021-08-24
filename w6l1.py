from netmiko import Netmiko
from getpass import getpass

csr1 = '10.100.100.3'
csr2 = '10.100.100.5'

devices = {
"host" : csr1,
"username" : 'admin',
"password" : 'cisco',
"device_type" : 'cisco_ios'
}

net_conn = Netmiko(**devices)
print(net_conn.find_prompt())





