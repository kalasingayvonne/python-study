fruits=['pineapple','apple','banana','mango','grapes']
print(fruits)
print(type(fruits))
#indexing and slicing
print(fruits[2])
print(fruits[-2])

#slicing-extracting a part of a list
#[start_index:end_index]
print(fruits[1:4])
print(fruits[2:5])

#updating
fruits[2]='watermelon'
print(fruits)

#append
fruits.append('strawberries')
print(fruits)

#insert
fruits.insert(1,'apples')

#remove
fruits.remove('mango')
print(fruits)

#pop
fruits.pop(0)
print(fruits)

#clear
fruits.clear()
print(fruits)


weekdays=['monday','tuesday','wednesday','thursday','friday']
print(weekdays[0])
print(weekdays[1:5])

weekdays[3]='thur'
print(weekdays)

weekdays.append('january')
print(weekdays)

weekdays.insert(2,'december')
print(weekdays)

weekdays.remove('friday')
print(weekdays)

weekdays.pop()
print(weekdays)

weekdays.pop(1)
print(weekdays)

weekdays.clear()
print(weekdays)