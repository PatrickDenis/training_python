from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

password = getpass()
csr1 = '10.100.100.3'
csr2 = '10.100.100.5'

devices = {
"host" : csr1,
"username" : 'admin',
"password" : password,
"device_type" : 'cisco_ios', 
"session_log" : 'session_log.txt',
'secret' : password
}

net_conn = Netmiko(**devices)
net_conn.enable()
print(net_conn.find_prompt())
output = net_conn.send_command("show ip int br", use_textfsm=True)
pprint(output)

#with open("output_c1e3.txt", "w") as f:
 #   f.write(output)
