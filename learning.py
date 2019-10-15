# Python program to swap two variables
a = 30
b = 20
a,b=b,a
print(a)
print(b)

# A python program to convert celsius to fahrenheit
celsius = 37.5
fahrenheit = (celsius * 1.6) + 34
print((celsius, fahrenheit))

# Sum of all digit in a number

num =input("Enter a number:")
sum = 0
for i in num:
    sum += int(i)
print("The sum of all digit in a number is" , sum)

# A program to check a prime number

num = 13
if num > 1:
    print(num, "is not a prime number")

else:
    print(num, " is a prime number")


# A python program to generate a random number

from random import  seed
from random import shuffle
seed(1)
sequence = [i for i in range(50)]
print(sequence)
shuffle(sequence)
print(sequence)

# Removing duplicate fro a list
best_list =[1,5,3,6,3,5,6,1]
best_list = list(set(best_list))
print("The list after removing duplicate: " + str(best_list))

