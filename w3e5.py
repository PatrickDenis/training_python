from pprint import pprint
def sep():
    print("*"*70)

base_ip = "10.10.100."

new_ip_list = []
for num in range(1, 255):
    ip = base_ip + str(num)
    new_ip_list.append(ip)

for i , ip_addr in enumerate(new_ip_list):
    print(i,"---->",ip_addr)

