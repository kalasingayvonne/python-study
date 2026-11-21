

name1="  JOHn  ."
name1=name1.replace('.', '')
name1=name1.strip()
name1=name1.lower()
print(name1)

sentence_one = "The Dog Breed is German Shepherd "
print(sentence_one[8:23])

sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two[16:30])

text='The lazy dog; ran so fast; it hit the wall.'
text=text.split(';')
print(text)
print(len(text))

first_name="    Joh.n  " 
last_name="     Do,e  " 
first_name=first_name.strip()
first_name=first_name.replace('.','')
last_name=last_name.strip()
last_name=last_name.replace(',','')
full_name=first_name+' '+last_name
print(full_name)

r = '["E","W","C"]'
r=r.replace(',','')
r=r.replace('"','')
r=r.replace('[','')
r=r.replace(']','')


print(r)