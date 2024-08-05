# # TASK 6: Using Python or PHP or Java or Ruby or JavaScript
# # Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message, the account is blocked.
# # Once you learn functions, revisit this and write this code inside a function.
# correct_password = "admin@123"
# attempts=4
# for i in range(attempts):
#     pasword = input("enter password: ")
#     if pasword==correct_password:
#         print("access granted")
#         break
#     else:
#         rem_att=attempts-(i+1)
#         if rem_att==0:
#             print("account is blocked")
#         else:
            # print(f'wrong passw password{rem_att} remaining')

speed_limit = 70
speed = int(input("enter speed: "))
demerit = 0
if speed <= speed_limit:
	print("ok")
elif speed > speed_limit and speed <= 75:
	demerit += 1
else:
	points =1 + (speed-75)/5
	demerit += points
print(demerit)
if demerit >= 12:
	print("suspended")
