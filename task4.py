#TASK 4: Using Python or PHP or Java or Ruby or JavaScript
#Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
#Once you learn functions,revisit this and write this code inside a function.


def valid_email(email):

    if "@" not in email or "." not in email:
        return False
    else:
        return True

user_email = input("Enter email: ")

if valid_email(user_email):
    print("valid email")
else:
    print("invalid email")
