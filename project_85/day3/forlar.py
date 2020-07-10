myList = []

for i in range(0, 10):
    myList.append(i)

print(myList)
name = "Ahmet"
len_name = len(name)
for i in name:
    if len_name != 1:
        print(i, end=", ")
    else:
        print(i, end="\n")
    len_name -= 1

sum_list = 0
for i in myList:
    sum_list += i

print(sum_list)
