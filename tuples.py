# create tuples
# enclosed with ()
my_tuple=("josh","tony","arnold","stanley",1000,99)
# list =>used to convert a data structure into a list
my_tuple=list(my_tuple)
print(my_tuple)
# tuple =>used to convert a data structure into a tuple
x=[1,2,3,4,5]
x=tuple(x)
print(type(x))

y=("a","b","c")
y=list(y)
y[2]='d'
y=tuple(y)
print(y)
days = ("monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday")
# 1. Find wednesday using an index
# 2. Using a function a find the length of the tuple.
# 3. Replace Thursday with Thur
