# A python program that calculate ones age

import  datetime
name = input("Enter your name:")
age = input ("Enter your age: ")
now = datetime.datetime.now()
diff = 80 - int(age)
print("hi" + name + "you will complete 80 years in"(now.year + diff))

