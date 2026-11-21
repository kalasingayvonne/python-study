#Write a program that takes the email and password as input from a user and 
# checks if they are equal to “admin@mail.com” and password is “Admin@123” , 
# if so then print  “Login is Successful” and 
# if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.

def valid_login(email, password):
    return email == "admin@mail.com" and password == "Admin@123"

attempts = 3
success = False

for i in range(attempts):
    user_email = input("Enter email: ")
    password = input("Enter password: ")

    if valid_login(user_email, password):
        print("Login is Successful")
        success = True
        break
    else:
        print("Invalid username or password")

if not success:
    print("You have been blocked")