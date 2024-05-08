text = "apple banana orange apple banana watermelon throw"
word_count = {}

words = text.split()
for word in words: # loop through list
    if word in word_count: #check if key exsitst
        word_count[word]+=1
    else:
        word_count[word] = 1

print(word_count)