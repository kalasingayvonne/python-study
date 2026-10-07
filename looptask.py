#Write a program that displays a numbers 1 to 50 inside a list.

numbers=list(range(1,51))
print(numbers)


#From 1 above display the ones divisible by 7 or 5 inside a list.

numbers=list(range(1,51))
num=[]
for n in numbers:
    if n%5==0 or n%7==0:
        num.append(n)
print(num)


#Find sum and average of values in the range between 10 to 40.

values=list(range(10,41))
total=0

for v in values:
    total=total+v
    print(total)

average = total / len(values)

print(average)

#Put in a list the first 10 odd numbers between 10 to 50. 

numbers1=list(range(10,51))
num1=[]

for i in numbers:
    if i%2!=0:
        num1.append(i)
    if len(num1) == 10:
        break
print(num1)

#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.

number = int(input("Enter a number: "))

numbers=(range(1,11))

for i in numbers:
    mult=numbers i
    print(f"{numbers} x {i} = {numbers*i}")

#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even=range(1,51)
count = 0

for i in even:
    if i % 2 == 0:
     count +=1

print(count)

#ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#Display the total quantity of the 3 above.

ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32')]
total_quantity=0

for i in ls1:
 quantity=int(i[1])
total_quantity=total_quantity+quantity
print(total_quantity)

#Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. 
# After you show them a message , the account is blocked.

correct_password = "admin@123"

lst4=list(range(1,5))

print(lst4)

attempts=4
for p in lst4:
    pin=input('Enter your pin:')
    corect_pin='admin@123'
    if pin==corect_pin:
     print('acess granted')
     break
    else:
     rem_att=attempts-p
     if rem_att==0:
      print('acc blocked')
     else:
      print(f'wrong pin you have {rem_att} attempts remaining')