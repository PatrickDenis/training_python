from pprint import pprint
import re

def sep():
    print("*"*70)
    
with open("show_version.txt", "r") as f:
    shv = f.read()
    
#print(shv)
    
match = re.search(r"^Cisco IOS Software,.* Version.(\d.+)\S\sR", shv, flags=re.M)
if match:
    os_version = match.group(1)
print(f"Os Version is :{os_version}")
      
match = re.search(r"^Processor.+ID\s(.*)\s", shv, flags=re.M)
if match:
    Serial_Number = match.group(1)
print(f"Serial Number is :{Serial_Number}")


match = re.search(r"^Confi.+is\s(.*)", shv, flags=re.M)
if match:
    Conf_reg = match.group(1)
    print(Conf_reg)
print(f"Configuration Register is :{Conf_reg}")