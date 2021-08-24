from pprint import pprint
import re

def sep():
    print("*"*70)
    
with open("show_ipv6.txt", "r") as f:
    ipv6 = f.read()
    
#print(shv)
    
match = re.search(r"IPv6 address:\s+(.*).+\s+(.*)\s", ipv6, flags=re.M)
if match:
    ip1 = match.group(1)
    ip2 = match.group(2)
    print(f"ipv6_1 is :{ip1}")
    print(f"ipv6_2 is :{ip2}")
      
