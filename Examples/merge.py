dict1 = {"Rice": 10, "Fufu": 21, "Apples": 20, "Eru": 39}
dict2 = { "Fufu": 10, "Rice": 11, "Eru": 12, "Apples": 20,   "Orange": 41}

# Target: Merge these 2 dictionaries

merged = {}
for key in dict1:
  if key in dict2:
    merged[key] = dict1[key] + dict2[key]
  else:
    merged[key] = dict1[key]

print(merged)