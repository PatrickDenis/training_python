from netmiko import Netmiko
from getpass import getpass

password = getpass()

csr1 = host='10.100.100.3', username='admin', password=getpass(), device_type='cisco_ios'
csr2 = host='10.100.100.5', username='admin', password=getpass(), device_type='cisco_ios'


devices = [csr1, csr2]


for device in devices:
    net_conn = Netmiko(**device)
    net_conn.enable()
    
    print("Step 1 showing the prompt")
    print(net_conn.find_prompt())
    print("Trying a send command")
    show_version = net_conn.send_command('show version')
    test = show_version.splitlines()
    pprint(test)

