first_name="kevin"
second_name="ropy"
age=25


# type function to find the datatype
age=str(age)

# str is used to covert data into a string
print(type(age))
full_name=first_name + " "+ second_name
# print(full_name)

# accessing characters in a string
# indexing 
# from right you start with -1
# from the left we start with 0
# square brackets []

full_name="kevin Ropy"
# print(full_name[-4])

# slicing
# => extract a substring
# print(full_name[6:10])

# String methods
# =>used to manipulate strings
# full_name = "kevin Ropy"

# f1=full_name.upper()
# print(f1)
# f2=f1.lower()
# print(f2)
# f3=f2.capitalize()
# print(f3)

# f4=full_name.find("R")
# print(f4)
# strip
# =>used to remove leading and trailing spaces 
class_name=" November intake           "
cl=class_name.strip()

print(len(class_name))
print(len(cl))

# replace(old,new)
last_name="Kevin Ro----py"
last_name=last_name.replace("-","")
print(last_name)

# split
names="arnold:tony:Pendo"
print(names.split(':'))
# count
x="techcamp coding"
print(x.count("c"))







