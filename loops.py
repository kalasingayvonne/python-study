#for loop
fruits=['pineapple','apple','banana','mango','grapes']

for fruit in fruits:
    print('fruits')

numbers=[10,20,30,40,50]
for i in numbers:
    print(i)

nums=[100,200,300,400,900]
for i in nums:
    print('hello world')

#display name ten times
mylist=[10,20,30,40,50,60,70,80,90,100]
for i in mylist:
    print('yvonne')

#range
numbers=list(range(1,101))

for i in numbers:
    print('techcamp')

#display even numbers btn 10 and 50
lst=list(range(10,51))
even_numbers=[]
for i in lst:
    if i%2==0:
     even_numbers.append(i)
    
print(even_numbers)

#display numbers between 100 and 150 that are divisible by 5

lst1=list(range(100,151))

for i in lst1:
    if i%5==0:
        print(i)

#dispaly odd numbers btn 30 and 100

lst2=list(range(30,101))
odd=[]
for i in lst2:
    if i % 2 !=0:
        odd.append(i)
print(odd)

#display numbers between 1-100 divisible by 3 and 5 in a list

lst3=list(range(1,101))
num=[]
for d in lst3:
    if d%3==0 and d%5==0:
        num.append(d)
print(num)

#sim manager example
lst4=list(range(1,4))
print(lst4)
attempts=3
for p in lst4:
    pin=input('Enter your pin:')
    corect_pin='1234'
    if pin==corect_pin:
     print('acess granted')
     break
    else:
     rem_att=attempts-p
     if rem_att==0:
      print('acc blocked')
     else:
      print(f'wrong pin you have {rem_att} attempts remaining')