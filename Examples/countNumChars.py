# Count the number of occurence of a character in a string
myString = input("Input the String: ")

char_freq = {}

for char in myString:
    if char in char_freq:
        char_freq[char]+=1
        print(char_freq)
    else:
        char_freq[char] = 1
        print(char_freq)

# myNew = list(myString)
# freq = [myNew.count(i) for i in myNew]
# print(myNew)
# print(freq)
# count = dict(zip(myNew, freq))
# print(count)





