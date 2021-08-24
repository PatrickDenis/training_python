from pprint import pprint
def sep():
    print("*"*70)
    
net_device = {
    "ip_addr": "10.100.100.3",
    "vendor": "Cisco",
    "password": "cisco",
    }

bgp_fields = {
    "bgp_as": "400",
    "peer_as": "401",
    "peer_ip": "10.100.100.5",
}

print(net_device["ip_addr"])

if net_device["vendor"] == "Cisco":
    net_device = {"platform": "ios"}
elif net_device["vendor"] == "Juniper":
    net_device = {"platform": "JunOs"}
    
print(net_device["platform"])
sep()

net_device.update(bgp_fields)
print(net_device)

sep()

for k in net_device.keys():
    print(k)
sep()

for k, v in net_device.items():
    print(k, v)
    
     



