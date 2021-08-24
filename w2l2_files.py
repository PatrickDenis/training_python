
from os import fchown


with open("test.txt", "w") as f:
   new = f.write('a ben caliss')
   ah = f.read()
print(ah)
