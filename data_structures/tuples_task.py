#create a new file tuples_task.py
#1. numbers = (10, 20, 30, 40, 50)Add 60 to the end,Replace 30 with 35.
#2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order.
#3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
#Count occurrences of "banana",Remove all occurrences of "banana".
#4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order of elements using sort method.
#5. colors = ("red", "blue", "green")add "yellow" at index 1,Extend with ["purple", "orange"]

numbers = (10, 20, 30, 40, 50)

numbers=list(numbers)
print(type(numbers))

numbers.append('60')
print(numbers)

numbers[2]='35'
print(numbers)

numbers=tuple(numbers)
print(type(numbers))

values = (15, 5, 30, 25, 10)
values=list(values)
print(type(values))

values.sort()
print(values)

values=tuple(values)
print(type(values))

fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")

print(fruits.count('banana'))

fruits=list(fruits)

print(type(fruits))

fruits.remove('banana')
fruits.remove('banana')
fruits.remove('banana')
print(fruits)


fruits=tuple(fruits)
print(type(fruits))


names = ("Alice", "Bob", "Charlie", "David")
names=list(names)
print(names)
names.sort(reverse=True)
print(names)
names=tuple(names)
print(type(names))

colors = ("red", "blue", "green")
colors=list(colors)
print(colors)

colors.insert(1,'yellow')
print(colors)

colors2=("purple", "orange")
colors.extend(colors2)
print(colors)

colors=tuple(colors)
print(type(colors))
