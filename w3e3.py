from pprint import pprint
import sys

def sep():
    print("*"*70)

with open("show_lldp_neighbors_detail.txt", "r") as f:
    output = f.read()

new = output.splitlines()
#pprint(new)

system_name = ''
port_id = ''
for each_line in new:
    if "System Name: " in each_line:
        system_name = each_line
    elif "Port id: " in each_line:
        port_id = each_line
    elif system_name != '' and port_id != '':
        break

print(system_name,port_id)

