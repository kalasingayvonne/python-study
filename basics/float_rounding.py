#Questions create a new file
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 
 
temp=56.8926
print(round(temp))

temp= 56.8926
print(round(temp,2))

temp=56.8926 
print(round(temp,3))


temp1=56.8926
temp1=str(temp)
print(temp1[3:])
temp1=temp1[3]+'.'+ temp1[4:]
print(temp1)
temp1=float(temp1)
print(type(temp1))

