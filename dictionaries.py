
student1={
'name':'mike',
'age':21,
'country':'kenya',
'gender':'male',
'name':'alex',
'hobbies':['hiking','painting','cycling']
}
print(type(student1))
print(student1['name'])

#add and update properties
#add

student1['city']='nairobi'
student1['county']='kisumu'
print(student1)

#update
student1['age']=30
print(student1)

student1['name']='txunami'
student1['country']='Egypt'
print(student1)

#add new key skills with values['py','web dev','UI']
student1['skills']=['py','web dev','UI']

print(student1['skills'][1])
print(student1['hobbies'])


#keys
print(student1.keys())
#values
print(student1.values())
#items
print(student1.items())
#get
print(student1.get('age'))#used in projects cause it does not return an error
