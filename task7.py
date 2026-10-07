#Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

def student_marks(marks):
 if marks>79:
   return 'A'
 elif marks>=60:
  return 'B'
 elif marks>=50:
  return 'C'

 elif marks>=40:
  return 'D'

 else:
  return 'E'
 
marks=int(input('Enter marks:'))

if marks < 0 or marks> 100:
    print("Invalid marks. Enter a value between 0 and 100.")
else:
    print("Grade:", student_marks(marks))