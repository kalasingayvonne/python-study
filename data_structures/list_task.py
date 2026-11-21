
#1. Display 2 from the list.
trainees= ["John", [2, ["James","Mary"]]]
print(trainees[1][0])

#Output James  from the list.
trainees= ["John", [2, ["James","Mary"]]]
print(trainees[1][1][0])

# Using a method add 56 at the end of the list.
trainees.append('56')
print(trainees)

# Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,'Mike')
print(trainees)

#Change the value of 2 to 8
trainees[1][0]='8'
print(trainees)

#Remove John and Mary from the list.
trainees[1][1].remove('Mary')
trainees.remove('John')
print(trainees)


# Using a function, determine the length of the list
print(len(trainees))

#employees = [ "TechElar",[4, ["Kevin", "Brian", "Alice"]]]

# 1. Display the number 4.


# 2. Display "Brian" from the list.


# 3. Display "Alice" from the list.


# 4. Using a list method, add the number 7 at the end of the outer list.


# 5. Add "David" between "Brian" and "Alice".


# 6. Change the number 4 to 10.


# 7. Change "Kevin" to "James".


# 8. Remove "TechElar" from the list.


# 9. Remove "Alice" from the nested list.


# 10. Add "Mary" at the beginning of the nested list.


# 11. Using len(), find the number of items
#     in the nested employee list.


# 12. Print the final list.

employees = [ "TechElar",[4, ["Kevin", "Brian", "Alice"]]]

print(employees[1][0])

print(employees[1][1][1])

print(employees[1][1][2])

employees.append('7')
print(employees)

employees[1][1].insert(2,'david')
print(employees)

employees[1][0]='10'
print(employees)

employees[1][1][0]='james'
print(employees)

employees.remove('TechElar')
print(employees)


employees[0][1].remove('Alice')
print(employees)

employees[0][1].insert(0,'Mary')
print(employees)

print(len(employees[0][1]))

print(employees)