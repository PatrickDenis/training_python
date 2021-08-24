
var1 = "cisco"
var2 = "881"
show_version = "\"*0        CISCO881-SEC-K9       FTX0000038X    \""
show_version = show_version.strip()
print(var1.upper() in show_version)
print(var2 in show_version)
show_version = show_version.strip().split()
print(show_version[1],show_version[2])