# how to create lists 
students=["Vera","Arnold","Andrew","Pendo",100,1000,True,False]
print(type(students))
print(students)
#create a list of months  display on the terminal
months=["jan","feb"]
# Accessing elements in a list 
students = ["Vera","Arnold","Andrew",["a","b",99,["mango",["ginger",1000],"banana"]],"Pendo",100]
print(students[3][2])
print(students[3][3][1])
print(students[3][3][1][1])

# modifying elements in a list
numbers=[1,2,3,4,5]
numbers[4]="mango"
numbers[1]="orange"
print(numbers)

# slicing
fruits=["oranges","banana","mangoes","apple","grapes","limes"]
print(fruits[1:3])
print(fruits[4::-2])

# lists methods
# =>used to manipulate strings
fruits = ["oranges", "banana", "mangoes", "apple", "grapes", "limes"]
# append
fruits.append("tomato")
# clear
# copy

x=fruits.copy()
print(fruits.count("banana"))
fruits.insert(1,"ginger")
print(fruits.index('mangoes'))
fruits.pop(3)
print(fruits)

