person = {"name": "Andrew", "age":49, "address": "Bamenda"}

# print(person)

# if "dob" in person:
#     print("DOB is a key in the dictionary")
# else:
#     print("Key does not exist")

# print(person['name'])
# print(person['age'])

# # person.clear()
# new_person = person.copy()

# # print(person)
# # print(new_person)

# # print(person['dob'])
# if "dob"  not in person:
#     print("No key found")

# else:
#     print(person['dob'])

# print(person.get('dob', "2023-05-05"))

# print(person.items())
# print(person.keys()) [keys]
# print(person.values()) [values]


# person['name'] = "Jousaine" # update
# print(person)

# person['dob'] = "2024-09-08" #append
# print(person)


#List have Append
# Dictionaries do not have append


# Looping through a dictionary
for key in person.keys(): # all the keys
    print(key)

# Looping through a dictionary
for value in person.values(): # all the values
    print(value)

for key, value in person.items(): # all keys and values
    print(key, value)

listOfKeys = list(person.keys())
listOfKeys = list(person.values())