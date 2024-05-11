# Assuming that we had a list of items, say 1, 2, 4 
# Our goal is to calculate the sum of all the itemss in the list

listOfItems = []
while(True):
    item = input("Enter number and press q to exit: ")
    if(item == "q"):
        break
    listOfItems.append(int(item))
    print(listOfItems)

# allSum = sum(listOfItems)

# print(allSum)
total = 0
count = 0
for i in listOfItems:
    total+=i
    count+=1
print(total)
print(count)
