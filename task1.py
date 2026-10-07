# 1: Using Python or PHP or Java or Ruby or JavaScript
#Write a program that prompts the user to enter the base and height of a triangle and returns its area.

def triangle_area(base, height):
    area=0.5 * base * height
    return area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))


triangle=triangle_area(base,height)
print(triangle)



