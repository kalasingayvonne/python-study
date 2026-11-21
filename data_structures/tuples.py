fruits=('apple','banana','carrot','mango','kiwi')

print(type(fruits))
print(fruits[2])

fruits=list(fruits)
print(type(fruits))

fruits[1]='strawberries'
print(fruits)

fruits.append('watermelon')
print(fruits)

fruits=tuple(fruits)
print(type(fruits))


#days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
#2. Using a function a find the length of the tuple.
#3. Replace Thursday with Thur

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
print(days[2])
print(len(days))

days=list(days)
print(type(days))

days[3]='thur'
print(days)

days=tuple(days)
print(type(days))