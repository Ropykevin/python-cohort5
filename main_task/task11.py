# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years, months, days TODAY.
import datetime

today=datetime.datetime.now()
dob=input("enter your dob (year/month/day):  ")
print(dob)
dob_split=dob.split("/")
dob_year=int(dob_split[0])
dob_month=int(dob_split[1])
dob_day=int(dob_split[2])

years = today.year-dob_year
months=today.month-dob_month
days=today.day-dob_day
# negative days

if days < 0:
    months -= 1
    # Get the number of days in the last month
    if today.month>1:
        last_month = today.month - 1
        if last_month != 12:
            last_month_year = today.year
        else:
            last_month_year=today.year - 1
    else:
        last_month = 12
    
    days += (datetime.datetime(last_month_year, last_month, 1) -
             datetime.timedelta(days=1)).day

        #    negative months #
if months<0:
    years-=1
    months+=12
    

print(f"{years} years {months} months and {days} days")

