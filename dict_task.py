# 5. Reverse 987 to 789 without using an inbuilt - method or Assigning 789 manually.
my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency": "KES"}], 987, (76, "John")]
# get to 987
print(type(my_ds[4]))
# convert to a string
my_ds[4]=str(my_ds[4])
print(type(my_ds[4]))
# reverse using [::] 987 to 789
my_ds[4]=my_ds[4][2::-1]
# convert it back into a number
my_ds[4]=int(my_ds[4])
print(my_ds)
# Hint: Strings can be reversed using[::]
# 6. Change the name “John” to “Jane” .
# get to the tuple  john
print(my_ds[5])

# convert to list
my_ds[5]=list(my_ds[5])
# change john to jane
my_ds[5][1]="jane"
# convert it back to  tple
my_ds[5]=tuple(my_ds[5])
print(my_ds)

# my_ds[5] = my_ds[5][0], "Jane"
# print(my_ds)

# You can research or discuss to find the solutions above.
# https: // realpython.com/quizzes/pybasics-tuples-lists-dicts/
