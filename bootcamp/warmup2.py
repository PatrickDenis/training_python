


def animal_carckers(name1,name2):
    #name1 = name1.upper([0])
    #name2 = name2.upper([0])
    
    if name1[0].upper() == name2[0].upper():
        print(name1,name2)
        print("True")
        return True
    else:
        print(name1,name2)
        print("False")
        return False
    
animal_carckers("veau","Vache")