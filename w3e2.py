from pprint import pprint

def sep():
    print("*"*70)

with open("ip_arp.txt", "r") as f:
    output = f.readlines()


for each_lines in output:
    ip = each_lines.split()[1]
    mac = each_lines.split()[3]
    if ip == "10.220.88.1":
        print(f"This is the default GW ({ip})")
        continue
    if ip == "Address":
        continue
    result = [ip,mac]
    print(result)
