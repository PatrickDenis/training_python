


def myfunc(my_string):
    new_string = []
    position = 0
    
    for each_char in my_string:
        if position % 2 == 0:
            new_char = each_char.upper()
            new_string.append(new_char)
        else:
            new_string.append(each_char)
        position += 1
    new_string = ''.join(new_string)
    print(new_string)
    return new_string

myfunc("hello mister big")



