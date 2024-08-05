# # def hello():
# #     name = "kevin"
# #     print(f"Hello, {name}!")
# # hello()


# def hello(name):
#     return(f"Hello, {name}!")
    

# # hello("kevin")
# # hello("ken")
# full_name=input("enter your name")
# x = hello(full_name)
# print(x)

# # create a function to calculate the area of a triangle use parameters 2
# def triangle_area(a, b):
#     area=(a*b)*0.5
#     return area

# base=int(input("enter base: "))
# heigth=int(input("enter heigth: "))
# tr_area=triangle_area(base,heigth)
# print(tr_area)
# # create a function that calculates the area of a rectangle take users input use parameters
# def rectangle_area(x,y):
#     area=x*y
#     return area
# # get user input
# length=int(input("enter length: "))
# width=int(input("enter width: "))
# # call the function and print the result
# rect_area=rectangle_area(length,width)

# print(rect_area)

# # create  a function that takes input from a user of a num and checks if the number is an even number

# def check_number(num):
#     if num % 2 == 0:
#         result=f"{num} is even"
#     else:
#         result=f"{num} is odd"
#     return result

# number=int(input("enter number: "))
# c_number=check_number(number)

# print(c_number)

# 3,8,10,12,13 using functions parameters
# 13,

# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C  # or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123”, if so then print “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions, revisit this and write this code inside a function.
# parameters => 2 email,password
# 
def check_logins():
    correct_email ='admin@mail.com'
    correct_password = "Admin@123"
    attempts=3
    for i in range(attempts):
        email = input("enter email: ")
        password = input("enter password: ")
        if email==correct_email and password==correct_password:
            output = "Login is Successful"
            break
        else:
            remaining_tries= attempts-(i+1)
            if remaining_tries<=0:
                output="you have been blocked"
            else:
                print(f"invalid email or password try again {
                    remaining_tries} tries remaining")
                      
    return output

# get user input
result=check_logins()
# print(result)
# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’, ’30kshs’, ’300’], [‘milk’, ’50kshs’, ’200’], [‘bread’, ’45kshs’, ’359’], [‘coffee’, ’5kshs’, ’79’]]


def calc_stock(a):
    total_stock=0
    for i in a:
        stock=int(i[2])
        total_stock+=stock
    return total_stock


prods = [["omo", "30kshs", "300"], ["milk", "50kshs", "200"], ["bread", '45kshs', '359'], ['coffee', '5kshs', '79']]

total_stock=calc_stock(prods)
print(total_stock)
