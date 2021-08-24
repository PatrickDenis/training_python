st = "Print only the words that start with S in this sentence"

new_st = st.split()
print(new_st)

for each_char in new_st :
    if each_char[0] == "s" or each_char[0] == "S":
        print(each_char)

print("------------------------------------")

nrange = range(0,11,2)
for each_num in nrange:
    print(each_num)

print("------------------------------------")

n2range = range(50)
for each_num2 in n2range:
    if each_num2 %3 == 0:
        print(each_num2)

print("------------------------------------")

nst = "Print every word in this sentence that has an even number of letters"
new_nst = st.split()

for each_word in new_nst:
    if len(each_word) %2 == 0:
        print(each_word)

print("------------------------------------")

n3range = range(100)
for each_num3 in n2range:
    if each_num3 %3 == 0 and each_num3 %5 == 0:
        print("FizzBuzz")
    elif each_num3 %3 == 0:
        print("Fizz")
    elif each_num3 %5 == 0:
        print("Buzz")
    else:
        print(each_num3)

print("------------------------------------")

mst = "Create a list of the first letters os every word in this string"
new_mst = mst.split()

new_list_mst = []

for each_words2 in new_mst:
    new_list_mst.append(each_words2[0])

print(new_list_mst)
