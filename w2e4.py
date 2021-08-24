from pprint import pprint


def sep():
    print("*"*70)

sep()
with open("show_ip_int_brief.txt", "r") as f:
    output = f.readlines()
pprint(output)
sep()
new_ouput = output[5].split()
pprint(new_ouput)
sep()
n2_output = tuple(new_ouput[:2])
pprint(n2_output)
sep()

