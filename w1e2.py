from pprint import pprint

def sep():
    print("-" * 72)

ip_addr = input("Please Enter an IP: ")
pprint(ip_addr)
sep()
octets = ip_addr.strip("\n").split(".")
print(octets)
sep()

sep()
print("{:^15}{:^15}{:^15}{:^15}".format("Octect1","Octect2","Octect3","Octect4"))
print(f"{octets[0]:^15}{octets[1]:^15}{octets[2]:^15}{octets[3]:^15}")
print(f"{bin(int(octets[0])):^15}{bin(int(octets[1])):^15}{bin(int(octets[2])):^15}{bin(int(octets[3])):^15}")
print(f"{hex(int(octets[0])):^15}{hex(int(octets[1])):^15}{hex(int(octets[2])):^15}{bin(int(octets[3])):^15}")
sep()