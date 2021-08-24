from netmiko import Netmiko
import re


my_devices1 = {
    "host": "10.100.100.3",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco",           
}

my_devices2 = {
    "host": "10.100.100.5",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco",         
}

'''my_devices3 = {
    "host": "10.100.100.5",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco",          
}'''

all_devices = [my_devices1,my_devices2]
for devices in all_devices:
    
    net_conn = Netmiko(**devices)
    net_conn.enable()
    output = net_conn.send_command("show version")
    print(net_conn.find_prompt())
    print("*"*70)

    match = re.search(r"^Confi.+is\s(.*)", output, flags=re.M)
    if match:
        Conf_reg = match.group(1)
        print(Conf_reg)
        print(f"Configuration Register is :{Conf_reg}")
