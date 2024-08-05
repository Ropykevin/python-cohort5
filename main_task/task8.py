# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit(70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
# Once you learn functions, revisit this and write this code inside a function.

def check_speed():
    speed_limit=70
    speed=int(input("enter speeed: "))
    demerit_points =(speed-speed_limit)/5
    max_demerit = 12
    if speed<=speed_limit:
        print("ok")
    elif demerit_points>max_demerit:
        print("license suspended")
    else:
        print("demerit points:",round(demerit_points))
        
check_speed()