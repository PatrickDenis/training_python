
#convert data structure [{}]

from netmiko import Netmiko
from getpass import getpass
from pprint import pprint



password = 'cisco'
csr1 = '10.100.100.3'
csr2 = '10.100.100.5'

devices = {
"host" : csr2,
"username" : 'admin',
"password" : password,
"device_type" : 'cisco_ios', 
"session_log" : 'session_log.txt',
'secret' : password
}

net_conn = Netmiko(**devices)
net_conn.enable()
print(net_conn.find_prompt())
output = net_conn.send_command("show cdp neighbor", use_textfsm=True)
pprint(output)
print(len(output)) #will help to see how many element in the list that become a dictionary after in this example

new_output = []
#creating new data structure out of this one

for k, v in output.items():
    print(k,   v)
    