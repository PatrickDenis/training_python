from pprint import pprint
def sep():
    print("*"*70)

Houston_ip = [
    "10.100.100.1",
    "10.100.100.2",
    "10.100.100.3",
    "10.100.100.4",
    "10.100.100.5",
    "10.100.100.1",
    "10.100.100.2",
    "10.100.100.3",
    "10.100.100.4",
    "10.100.100.5"
]

Atlanta_ip = [
    "10.100.100.1",
    "10.100.100.2",
    "10.100.100.3",
    "10.100.100.4",
    "10.100.100.5",
    "10.200.100.1",
    "10.200.100.2",
    "10.200.100.3",
    "10.200.100.4",
    "10.200.100.5"
]

Chicago_ip = [
    "10.100.100.1",
    "10.100.100.2",
    "10.100.100.3",
    "10.100.100.4",
    "10.100.100.5",
    "10.220.100.1",
    "10.220.100.2",
    "10.220.100.3",
    "10.220.100.4",
    "10.220.100.5"
]


Houston_ip = set(Houston_ip)
Atlanta_ip = set(Atlanta_ip)
Chicago_ip = set(Chicago_ip)

Duplicate_HA = Houston_ip & Atlanta_ip 
print(Duplicate_HA)

set()
print("1 - Duplicate IPs at all three sites:\n\n{}".format(Houston_ip & Atlanta_ip & Chicago_ip))
#I dont like to use that format, i prefer this way....grrr :P

print(f"2 - Duplicate IPs at all three sites:{Houston_ip & Atlanta_ip & Chicago_ip}")


