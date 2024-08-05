# looping through a dictionary
# dictionary is a collection of key value pair
person = {
    "name": "stan",
    'age': 20,
    "city": {"str": "hddh", "loc": "gggg"},
    'location': "corner house"

}
person2 = {
    "name": "arnold",
    'age': 29,
    "city": {"str": "hddh", "loc": "gggg"},
    'location': "kiambu"

}

# we loop through keys and values
for key, value in person.items():
    print(f"{key}:{value}")
    if key=="city":
        for i,x in person["city"].items():
            print(f"{i}:{x}")


for key in person.keys():
    print(key)

for i in person.values():
    print(i)

# zip function
for (key, value), (key1, value1) in zip(person.items(), person2.items()):
    print(key, value)
    print(key1, value1)
