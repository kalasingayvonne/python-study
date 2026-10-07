#TASK 3: Using Python or PHP or Java or Ruby or JavaScript
#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”


def phone_number(number):
 number = number.strip()
 if number.startswith("+254"):
        return number
 elif number.startswith("254"):
        return "+" + number
 elif number.startswith("07") or number.startswith("01"):
        return "+254" + number[1:]
 elif number.startswith("7") or number.startswith("1"):
        return "+254" + number
 else:
        return None

number = input("Enter phone number: ")
result = phone_number(number)

if result:
    print(result)
else:
    print("Invalid phone number")
