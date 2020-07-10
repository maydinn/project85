import datetime

my_time = datetime.datetime.now()

print(my_time)

print(my_time.month)

birth_date = datetime.datetime(1992, 12, 11)

print(birth_date)

print(my_time.strftime("%w"))
print(my_time.strftime("%a"))
print(my_time.strftime("%A"))
print(my_time.strftime("%B"))
print(my_time.strftime("%y"))
print(my_time.strftime("%H"))
print(my_time.strftime("%c"))
print(my_time.strftime("%x"))
print(my_time.strftime("%X"))

