# Ask the user for 2 numbers and print the avarage
try:
    num1 = float(input("input the first number "))
    num2 = float(input("Enter the second "))
    # get the avrage of 2 number
    average = (num1 + num2) / 2

    print(f"Average: {average}")
except ValueError:
    print("Invalid input, please enter either a float or an int")


