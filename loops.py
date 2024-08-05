# for loops


# display odd numbers from 0 1000 using loops
# break used to stop loop
# continue
odd_numbers = []
numbers = list(range(1000))
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)

# itterate throu numbers btw 20 500 display even
numbers2 = list(range(20, 500))
for num in numbers2:
    if num % 2 == 0:
        print(num)

# looping through list
x = [1, 2, 3, 4, 5]
for i in x:
    print(i)

fruits = ["mango", "orange", "banana"]
for i in fruits:
    print(i)

# Q5 Write a python program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".

x = list(range(1, 100))
for i in x:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
