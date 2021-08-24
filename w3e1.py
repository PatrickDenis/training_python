from pprint import pprint

def sep():
    print("*"*70)

with open("show_vlan.txt", "r") as f:
    output = f.readlines()
 
for each_line in output:
    if "-----" in each_line:
        continue
    new_list = tuple(each_line.split()[:2])
    pprint(new_list)

