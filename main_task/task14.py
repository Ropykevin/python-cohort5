# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions, revisit this and write this code inside a function.
while True:
    num1=input("enter a number1: ")
    num2 = input("enter a number2: ")
    if num1.isdigit() and num2.isdigit():
        num1=int(num1)
        num2=int(num2)
        sum=num1+num2
        break
    elif "." in num1 and "." in num2:
        num1=float(num1)
        num2=float(num2)
        sum=num1+num2
        break
    else:
        print("invalid character entered")

print(sum)

