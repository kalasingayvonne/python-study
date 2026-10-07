#calculate the area of a square using a function

def square_area(side):
    area=side*side
    print(area)
square_area(6)
square_area(9)

#print area of a circle

def circle_area():
    pi=3.14
    radius=6
    area=pi*radius*radius
    print(area)

circle_area()

def hello(name):
    print(f'hello {name}')
hello('txunami')

#create a function that calculates thhe area of a rectangle

def rectangle_area(length,width):
      area=length*width
      return area

rectangle1=rectangle_area(20,50)
print(rectangle1)
rectangle=rectangle_area(14,60)
print(rectangle)
