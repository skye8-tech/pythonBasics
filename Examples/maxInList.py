# Max number in a list of numbers
listOfNumbers = [12, 45, 2, 10, 19, 100]

#excelent approach 1
# maximum = max(listOfNumbers)

# print(f"Maximum is {maximum}")


# approach 2
maximum = listOfNumbers[0]
for num in listOfNumbers:
    if num > maximum:
        maximum = num
print(f"Max is {maximum}")
