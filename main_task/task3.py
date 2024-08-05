# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or 1.. Convert the number to start with +254…
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions, revisit this and write this code inside a function.
phone_number=input("enter phone number: ")
if phone_number[0:4]=="+254" and len(phone_number)==13:
    valid=f"{phone_number} is valid"
elif phone_number[0:2]=="07" and len(phone_number)==10:
    phone_number="+254"+phone_number[1:]
    valid = f"{phone_number} is valid"


print(valid)