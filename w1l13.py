


ip_addr = '192.168.1.1'
octects = ip_addr.rstrip("\n").split(".")

print("\n")
print("-" * 70)
print(f"{octects[0]:^20}{octects[1]:^20}{octects[2]:^20}{octects[3]:^20}")
print("-" * 70)
print("\n")
