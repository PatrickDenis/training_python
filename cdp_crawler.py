from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
import logging
import textfsm



    
def ip_list(command):

    username = input("Please enter your username :")
    password = getpass("Please enter your password: ")
    top_ip = input("Please enter an ip address : ")

    ip_list = []
    inventory = []

    ip_list.append(top_ip)
    #print(ip_list)


    for device in ip_list:

        my_device = {"host" : device, "username" : username, "password" : password, "device_type" : 'cisco_ios', 'secret' : password, 'fast_cli': True}
        net_conn = Netmiko(**my_device)
        net_conn.enable()
        output = net_conn.send_command("show cdp neighbor detail", use_textfsm=True)
        result = net_conn.send_command(command, use_textfsm=True)
        #new_result = (device, 'result of command', result)
    
             
        

        for element in output:
            for x,y in element.items():
                if "destination_host" in x:
                    host = y
                elif 'management_ip' in x:
                    ip = y
                else:
                    continue
            if ip in ip_list or " " in ip_list:
                continue

            new_ip_list = ip_list.append(ip)
            host_ip = [host+" : "+ip]
            inventory.extend(host_ip)

    else:
        print("DONE")
        print("*"*70)
        ip_list_str = str(ip_list)
        inventory_str = str(inventory)
        with open("inventory.txt", "w") as f:
            f.write(inventory_str)
        #pprint(inventory)
        print("*"*70)
        with open("ip_list.txt", "w") as f:
           f.write(ip_list_str)
        #pprint(ip_list)

    print("*"*70)
    return ip_list









            