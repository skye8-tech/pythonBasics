# initialize list for storing data
users = []

# variables to keep track of counts and ages
num_users = 0
total_ages = 0

# run the loop through until the user decides to quit
while True:
    try:
        # this is out of the loop
        name = input("Enter Name: ")
        age = int(input("Enter age: "))
        email = input("Enter email:")
        phone = input("Enter phone number:")
        address = input("Enter address:")

        if name.lower() == "q" or email.lower() == "q" or phone.lower() == "q" or phone.lower() == "q":
            break

        # creating a dictionary for the current user
        user_data = {"name": name, "age": age, "email": email,
                     "phone": phone, "address": address}
        users.append(user_data)

        # increase the counters
        num_users += 1
        total_ages += age
    except ValueError:
        print("Value Error")
        break

# calculate the average age
if (num_users != 0):
    average_age = total_ages/num_users
    print("total_users:", num_users)
    print("average age:", average_age)
    print("users:")
    print("Name \t\t | Age \t\t | Email \t\t | Phone \t | Address \t\t|")
    print("______________________________________________________________________")

    for user in users:
        print(
            f"{user['name']} \t | {user['age']} \t | {user['email']} \t | {user['phone']} \t | {user['address']} |")
        print("______________________________________________________________________")
