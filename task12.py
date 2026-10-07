#TASK 12: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that prints the largest of 4 inputs taken as input from a user.

def largest_input(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

nums = []
for i in range(4):
    nums.append(int(input(f"Enter number {i + 1}: ")))

print("The largest number is:", largest_input(nums))
