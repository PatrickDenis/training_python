

def old_macdonal(name):
    for each_letter in name:
        position = 0
        new_name = []

        if position == 0 or position == 3:
            new_letter = each_letter.upper()
            new_name.append(new_letter.upper())
            position += 1

        else:
            new_name.append(each_letter)
            position += 1
    new_name = ''.join(new_name)
    print(new_name)
    return new_name




old_macdonal("patrickdenis")
            

