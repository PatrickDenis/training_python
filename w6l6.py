from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


password = getpass()
csr1 = '10.100.100.3'
csr2 = '10.100.100.5'

devices = {
"host" : csr1,
"username" : 'admin',
"password" : password,
"device_type" : 'cisco_ios',
'secret' : password,
'fast_cli': True
}

net_conn = Netmiko(**devices)
net_conn.enable()
print(net_conn.find_prompt())

cfg_commands = ["int lo0", "desc test1"]

output2 = net_conn.send_config_set(cfg_commands)
output3 = net_conn.send_config_from_file("commands.txt")

output = net_conn.send_command("show ip int br", use_textfsm=True)
pprint(output)
print("*"*70)
print(output2)
print(output3)
