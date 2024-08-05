def hello():
    name="kevin"
    print(f"Hello, {name}!")
hello()
# create a function to calculate the area of a triangle 

def area_triangle():
    base=20
    height=10
    area=(base*height)*0.5
    print(area)
area_triangle()

# create a function that calculates the area of a rectangle take users input
def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(area)
area_rectangle()

# create  a function that takes input from a user of a num and checks if the number is an even number
def check_number():
    num = int(input("Enter a number: "))
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

check_number()

# 3,8,10,12,13 using functions

10
