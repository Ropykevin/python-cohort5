person={"name":"kevin",
        "age":25,
        "location":"Kiambu"}

# unordered
# accessing values
# by refering to their keys
print(person["name"])

# adding values to a dictionary
person["occ"]="doctor"
print(person)

details={
    'name':"josh",
    "class": "4N",
    "ADM":5496,
    "addr":{
        "code":20200,
        "street":"kimathi"
    },
    "subjects":["eng","ksw","comp"],
    "results":("A","B")

}
print(details["subjects"][1])#ksw
print(details["addr"]["street"])

# add town to addr
details["addr"]["town"] = "Kikuyu"
print(details["addr"])
# add chemistry to subjects
details['subjects'].append('chemistry')
print(details['subjects'])
print(details)
# remove
del details["results"]
details["subjects"].remove("ksw")
print(details)
# dictinary methods
person = {"name": "kevin",
          "age": 25,
        "location": "Kiambu"}
# Keys=>returns all the keys
print(person.keys())
# values =>returns all the values
print(person.values())
# items returns all the key-value pairs
print(person.items())
# clear 
# copy 


my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76, "John")]
print(my_ds[2])