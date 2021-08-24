def sep():
    print("*" *70)

ip1 = '10.100.100.1'
ip2 = '10.100.100.2'
ip3 = '10.100.100.3'
ip4 = '10.100.100.4'
ip5 = '10.100.100.5'

ip_list2 = ["10.100.100.9", "10.100.100.10"]

ip_list = [ip1,ip2,ip3,ip4,ip5]
print(ip_list)
sep()
ip_list.append('10.100.100.6')
print(ip_list)
sep()
ip_list.extend(["10.100.100.7","10.100.100.8"])
print(ip_list)
sep()
concatenate_list = ip_list + ip_list2
print(concatenate_list)
sep()
concatenate_list.pop()
print(concatenate_list)
sep()
concatenate_list[0] = "2.2.2.2"
print(concatenate_list)
sep()
