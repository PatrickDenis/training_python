from netmiko import Netmiko
#from getpass import getpass
from pprint import pprint
import logging
import textfsm

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")


#password = getpass()
csr1 = '10.100.100.3'
csr2 = '10.100.100.5'
csr3 = '10.100.100.1'

all_devices = [csr1]


for device in all_devices:
    
    my_device = {
    "host" : device,
    "username" : 'admin',
    "password" : "cisco",
    "device_type" : 'cisco_ios',
    'secret' : "cisco",
    'fast_cli': True
    }

    net_conn = Netmiko(**my_device)
    net_conn.enable()
    #print(net_conn.find_prompt())

    #cfg_commands = ["int lo0", "desc test1"]

    #output2 = net_conn.send_config_set(cfg_commands)
    #output3 = net_conn.send_config_from_file("commands.txt")

    output = net_conn.send_command("show cdp neighbor detail", use_textfsm=True)
    print(type(output))
    pprint(output)
    for element in output:
        for x,y in element.items():
            if "destination_host" in x or 'management_ip' in x:
                print(y)
            else:
                continue
            
        
    #print(output2)
    #print(output3)
