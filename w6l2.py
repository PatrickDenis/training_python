from netmiko import Netmiko
from getpass import getpass

password = getpass()
csr1 = '10.100.100.3'
csr2 = '10.100.100.5'

devices = {
"host" : csr1,
"username" : 'admin',
"password" : password,
"device_type" : 'cisco_ios',
'secret' : password
}

net_conn = Netmiko(**devices)
net_conn.enable()
print(net_conn.find_prompt())
print(net_conn.send_command("show version"))
