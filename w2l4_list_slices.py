

with open("show_version.txt", "r") as f:
    show_version = f.readlines() #will create a list with elements
print(type(show_version))
print(show_version)

for n in show_version:
    print(n)
    print(type(n))

