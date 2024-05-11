Elements = (1, 2, 3, 4, 5, 6)
Length = 0
Total = 0
for i in Elements:
    Length += 1
    Total += i
# Average is Sum of entire tuple / total number  items in the tuple
Average = Total / Length
print(Length)
print(Total)
print(Average)

average = sum(Elements) / len(Elements)
print(average)


