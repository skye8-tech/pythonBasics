# Remove Duplicate elements from a set
# data_set = [35, 35.5, 35.5, 36, 37, 37.5, 42.5, 36]
# unique_list = set(data_set)

# list_sq = [35, 35.5, 35.5, 36, 37, 37.5, 42.5, 36]
# unique_elements = []

# for element in list_sq:
#   if element not in unique_elements:
#     unique_elements.append(element)

# print(unique_elements)

list_sq = [35, 35.5, 35.5, 36, 37, 37.5, 42.5, 36]
unique_set = set()
for item in list_sq:
  unique_set.add(item)
print(unique_set)