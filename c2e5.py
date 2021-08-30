from netmiko import Netmiko
from netmiko import file_transfer
from getpass import getpass
from pprint import pprint
#from termcolor import colored


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


source_file = "session_log.txt"
dest_file = "dest.txt"
direction = "put"
file_system = "unix:"

net_conn = Netmiko(**devices)
net_conn.enable()
print(net_conn.find_prompt())
transfer_dict = file_transfer(
    net_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)
