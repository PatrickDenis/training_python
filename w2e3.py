from pprint import pprint
def sep():
    print("*"*70)

sep()
with open("ip_arp.txt", "r") as f:
    output = f.readlines()
    pprint(output)
    print(type(output))
sep()
output = output[1:]
pprint(output)    
sep()
output.sort()
pprint(output)
sep()
first_3_line = output[:3]
pprint(first_3_line)
sep()
new_output = "\n".join(first_3_line)
pprint(new_output)

with open("arp_entries.txt", "w") as f:
    final_output = f.write(new_output)


