print("ali")

print("bu \" dahası \t\t\t\tşimdi\nsonraki satır")


def this_way(name):
    print("hello", name)


this_way("ali")

this_way("mehmet")
list1 = ["ali", "can", "tan", "john"]
i = 0
while i < 2:
    list1.append(input("enter your name "))
    i += 1

for i in list1:
    if len(i) < 4:
        this_way(i)
    print("adı {}, size of ad {} ".format(i, len(i)))
