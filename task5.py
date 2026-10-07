#TASK 5: Using Python or PHP or Java or Ruby or JavaScript
#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
#  Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 

def large_number(a, b, c):
    largest = a

    if b > largest:
        largest = b

    if c > largest:
        largest = c

    return largest

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print( large_number(x, y, z))