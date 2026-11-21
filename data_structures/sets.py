fruits = {"apple","apple", "banana", "cherry", "banana", "mango", "banana"}

print(fruits)
fruits.add('kiwi')
print(fruits)

fruits.discard('mango') #or .remove
print(fruits)
#days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
#print(days)

#Remove friday and sunday from the set using methods.
#Add them back to the set

days= {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}

print(days)
days.remove('friday')
days.remove('sunday')

print(days)
days.add('friday')
days.add('sunday')
print(days)