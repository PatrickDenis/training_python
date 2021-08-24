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
output = net_conn.send_command("ping")
if '[ip]' in output:
    output += net_conn.send_command_timing("\n")
if 'address:' in output:
    output += net_conn.send_command_timing("10.100.100.1\n")
if 'count' in output:
    output += net_conn.send_command_timing("\n")
if 'size' in output:
    output += net_conn.send_command_timing("\n")
if 'seconds' in output:
    output += net_conn.send_command_timing("\n")
if 'commands' in output:
    output += net_conn.send_command_timing("\n")
if 'sizes' in output:
    output += net_conn.send_command_timing("\n")
    
print(output)
