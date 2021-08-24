from pprint import pprint
def sep():
    print("*"*70)

#this is a reminder for what does what since it is a bit confusing.
# i will be using a show_version.txt to test what does what... 

with open("show_version.txt", "r") as f:
    output = f.read() #will create a string that every character is an element
    #pprint(output)
    #print(type(output))
    #print("This return a string")

with open("show_version.txt", "r") as g:
    output2 = g.readline() #will read only the 1st line unless going through a forloop
    #pprint(output2)
    #print(type(output2))
    #print("This return a string")

with open("show_version.txt", "r") as h:
    output3 = h.readlines() #will create an element per line without removing the "\n"
    #pprint(output3)
    #print(type(output3))
    #print("This return a string")


pprint(output)
sep()
pprint(output2)
sep()
pprint(output3)
#sep()
#pprint(output.split("\n")) # return a list that split every word into element.
#sep()
#pprint(output.splitlines()) # return a list that split per line (\n) equivalent of a split("\n") command
sep()

new_output = output.upper()
print(type(new_output))
pprint(new_output)



