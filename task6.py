#TASK 6:Using Python or PHP or Java or Ruby or JavaScript
#Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.
# you learn functions,revisit this and write this code inside a function.

attempt=4
def user_password(valid_password,attempt):
    for i in range(attempt):
        password = input("Enter password: ")
        if password == 'admin@123':
            return True
        print(f"Wrong password. {attempt - i - 1} attempts left.")
    return False

if user_password("admin@123", 4):
    print("Access granted")
else:
    print("Account blocked")
