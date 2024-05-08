def greet(): # simple function that just prints out something
    name = input("whats your name")
    age = int(input("whats your age"))
    print(f"Hi there, your name is {name} and your age is {age}")

def greetPerson(name): # another type that takes in a parameter
    print("Hi there " + name)

def add(a, b):
    return a + b

def sum2(listItems):
    index = 0
    total = 0
    while(index < len(listItems)):
        total+=listItems[index]
        index+=1
    print(total)

def sum3(listItems):
    total = 0
    for item in listItems:
        total = total + item
    print(total)
        
myList = [1, 2,4, 56]     
sum2(myList) 
sum3(myList) 

# greetPerson("Andrew")

# add(5, 6)
# print(result)


# create a python program that ask a data entry staf at the hospital the number of patient he/she wants to collect data from,
# based on this number, define a dictionary to store the data, then loop based on the number times, collect the data and store in the dictionary

# expected data is , name, the age, location
# {"nameOfPerson": {age, location}}
# at the end, dispay the data in a tabular format format 

# eg
# Andrew  | 12    | Bamenda
# Jenice  | 11    | Douala

# display the sum of all the ages
# display the person with the highest age
