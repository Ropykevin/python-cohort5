# Write a program that displays  numbers 1 to 50 inside a list.
numbers_list = list(range(1, 51))
print(numbers_list)

# From 1 above display the ones divisible by 7 or 5 inside a list.
numberrs_divisible=[]
for i in numbers_list:
    if i % 7 == 0 or i % 5 == 0:
        numberrs_divisible.append(i)
print(numberrs_divisible)
# Find sum and average of values in the range between 10 to 40.


numbers=list(range(10,41))
total=0
for num in numbers:
    total+=num

print(total)
average=total/len(numbers)
# sum=sum(numbers)
# print(sum)
# average=sum/len(numbers)
# print(average)
# Put in a list the first 10 odd numbers between 10 to 50.
odd=[]
numbers=range(10,50)
for num in numbers:
    if num%2!=0:
        odd.append(num)
    if len(odd)==10:
        break
print(odd)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=int(input("enter a number: "))
for i in range(1,11):
    mult=i*number
    print(f"{i}*{number}= {mult}")
# t=1
# x=[]
# for  i in range(1,11):
#     if number>=0:
#         q=number*t
#         x.append(q)
#         t+=1
#         if t==11:
#             print(x)
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
count=[]
x = list(range(1, 51))
for i in x:
    if i % 2 == 0:
        print(i)
        count.append(i)

print(f"even numbers are {len(count)}")
# ls1 = [(“Jay”, 20), (“Mo”, 30), (“Mya”, 32)]
# Display the total quantity of the 3 above.

ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32),("x",50)]
total_quantity = 0
for i in ls1:
    print(i)
    quantity=i[1]
    # total_quantity=total_quantity+quantity
    total_quantity+=quantity

print(total_quantity)

# for name, quantity in ls1:
#     total_quantity += quantity
# print(f"The total quantity is: {total_quantity}")
