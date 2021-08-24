def sep():
    print("*" *70)

with open("show_version.txt", "r") as f:
    output = f.read()
    print(output)
    sep()
with open("show_version.txt", "r") as f:
    output2 = f.readlines()
    print(output2)
    sep()
