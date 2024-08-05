# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

# Use the value from total to get the average and average to find the grade.

# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

def calc_marks(maths, eng, swa, sci, sos):
    total = maths + eng + swa + sci + sos
    return total

maths=float(input("enter maths marks"))
english = float(input("enter eng marks"))
kiswahili = float(input("enter swa marks"))
science = float(input("enter sci marks"))
sos = float(input("enter sos marks"))

total_marks=calc_marks(maths,english,kiswahili,science,sos)
print(total_marks)

def calc_average(sum):
    average = sum / 5
    return average

average=calc_average(total_marks)
print(average)
