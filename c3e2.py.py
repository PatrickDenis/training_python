from netmiko import Netmiko
from getpass import getpass
from pprint import pprint



password = 'cisco'
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
output = net_conn.send_command("show spanning-tree", use_textfsm=True)
pprint(output)
print(len(output)) #will help to see how many element in the list that become a dictionary after in this example.
#print(output[1]['neighbor'])
root = ''
for element in output:
    if element['role'] == 'root':
        root = 'no'
        continue
    elif element['role'] == 'desg':
        root = 'yes'
if root == 'yes':
    print(f"This is a root Switch")
else:
    print(f"This isnt a root Switch, the root switch is toward {element['interface']}")