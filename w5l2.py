from netmiko import Netmiko
import re


csr1 = "10.100.100.1"
csr2= "10.100.100.3"
csr3 = "10.100.100.5"


all_devices = [csr1,csr2,csr3]

for device in all_devices:

    my_devices = {
    "host": device,
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
    "secret": "cisco",
    }
    
    net_conn = Netmiko(**my_devices)
    net_conn.enable()
    output = net_conn.send_command("show version")
    print(net_conn.find_prompt())
    print("*"*70)

    match = re.search(r"^Confi.+is\s(.*)", output, flags=re.M)
    if match:
        Conf_reg = match.group(1)
        print(Conf_reg)
        print(f"Configuration Register is :{Conf_reg}")
