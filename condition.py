# if statement
# else otherwise
a=5
b=10

if a>b:
    print("a is greater")
else:
    print("b is greater")

# task1
# take the users input of a number () input()
# check if the number is even
# if the number is not even display odd
# number=input("enter number: ")
# number=int(number)
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")

# task 2
# take the users input of a number () input()
# check if the number is odd and greater 30
# if the number is not odd display even
number1 = input("enter number: ")
number1 = int(number1)

if number1%2!=0 and number1>30:
    print("odd number and greater 30")
else:
    print("even number or less than 30")

# grading system 
# >80 A
# >70 <80 B
# >60 C
# else>D
# if elif else
# marks=int(input("enter marks: "))
# if marks>80:
#     print("grade A")
# elif marks>70 and marks<80:
#     print("grade B")
# elif marks>60 and marks<70:
#     print("grade c")
# else:
#     print("grade D")
    
# take users input of 3 numbers
# find the largest number on the 3 inputs
# assume the user 2 similar numbers
# num1 = int(input("enter number 1: "))
# num2 = int(input("enter number 2: "))
# num3 = int(input("enter number 3: "))

# if (num1>num2) and (num1>num3):
#     print(f"{num1} is the largest")
# elif (num2>num1) and (num2>num3):
#     print(f"{num2} is the largest")
# else:
#     print(f"{num3} is the largest")

# formatted strings allows you to insert variables inside a str

# nested if


# users input of marks
# check if marks are btw 0 and 100
# # >80 A
# >70 <80 B
# >60 C
# else>D
# else invalid marks

marks=int(input("enter marks: "))

if marks>=0 and marks<=100:
    if marks>80:
        print("grade A")
    elif marks>70 and marks<80:
        print("grade B")
    elif marks>60 and marks<70:
        print("grade c")
    else:
        print("grade D")
else:
    print("invalid marks")