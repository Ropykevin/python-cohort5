# Take three inputs from a user, separately. Print the largest of the numbers.
# input1=input("enter first number")
# input2 = input("enter second number")
# input3 = input("enter third number")
# input1=int(input1)
# input2=int(input2)
# input3=int(input3)

# if input1>input2 and input1>input3:
#     print(f"{input1} is the largest")
# elif input2>input1 and input2>input3:
#     print(f"{input2} is the largest")
# else:
#     print(f"{input3} is the largest")
# Hint: Determine what type of data is taken in as input.
# Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”, if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# temperature=input("enter the temperature")
# temperature=float(temperature)
# if temperature>30:
#     print("temperature is too high")
# elif temperature>15:
#     print("normal temperature")
# else:
#     print("cold temperature")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# x=input("enter x")
# y=input("enter y")
# x=float(x)
# y=float(y)
# if 20 >= x >= 10 and y > 100:
#     print("conditions met")
# else:
#     print("conditions not met")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is , print "Access   granted", otherwise print "Access denied"
# correct_password = "secret123"
# password=input("enter password")
# if password==correct_password:
#     print("access granted")
# else:
#     print("access denied")
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = int(input('Enter Student Score: '))
# attendance = int(input('Enter attendace: '))
# if student_score > 90:
#     if attendance > 80:
#         print('Excellent Student')
#     else:
#         print('Good score, but attendance needs improvement')
# else:
#     print('Poor')
# Attempt the questions in the link below
# https: // realpython.com/quizzes/python-conditional-statements/


# Question1: Write a Python program that checks if a variable num is positive. If it is, further check if it is divisible by both 2 and 3. Print appropriate messages for each case.
# num = int(input("enter num:"))
# if num > 0:
#     if num % 2 == 0 and num % 3 == 0:
#         print(f"{num} is positive and divible by 2 and 3")
#     else:
#         print("positive number but not divisible by 2 or 3")
# else:
#     print("negative number")
# Question2: Write a Python program that checks a username and password. If both are correct, print "Login successful". If either the username or password is incorrect, print "Login failed".

# username=input("enter username")
# password=input("enter password")
# correct_username="Kevin254"
# correct_password="123456"
# if username==correct_username and password==correct_password:
#     print("login successful")
# else:
#     print("login failed")

# Question3: Write a Python program that checks if a given string is a palindrome(reads the same forward and backward)

word=input("enter a word: ")
if word==word[::-1]:
    print("the word is a palindrome")
else:
    print("the word is not a palindrome")
# Question4: Write a Python program that calculates the Body Mass Index(BMI) and categorizes it into Underweight, Normal weight, Overweight, and Obesity based on standard BMI ranges.
# Question5: Write a Python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

# NB research on python loops
