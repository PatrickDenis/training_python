from pprint import pprint

def sep():
    print("*"*70)

with open("bgp.txt", "r") as f:
    output = f.read()
output = output.splitlines()
pprint(output)
as_number = output[0].split()[7]
print(as_number)
peer_ip = output[3].split()[0]
sep()
print(f"The AS is {as_number} and the Peer ip is {peer_ip}")
sep()