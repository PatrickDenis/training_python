mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1 = mac1.strip().split()
mac2 = mac2.strip().split()
mac3 = mac3.strip().split()

print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("-"*41)
print(f"{mac2[1]:>20}{mac2[3]:>21}")
print(f"{mac2[1]:>20}{mac2[3]:>21}")
print(f"{mac3[1]:>20}{mac3[3]:>21}")
print("-"*41)
print("-"*41)
print("-"*41)

mac_list = [mac1,mac2,mac3]
print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("-"*41)
for x in mac_list:
    print(f"{x[1]:>20}{x[3]:>21}")


