import os     #os commands
import shutil #shell utulity


with open("new_file.txt", "w") as f:
    f.write("this is a test string lol")

"""f = open("new_file.txt", "w+")
f.write("this is a test")
f.close"""

result = os.getcwd()
print(result)

result = os.listdir()
print(result)

result = shutil.copy(src,dest) # shutil.var(src,dest)
print(result)

