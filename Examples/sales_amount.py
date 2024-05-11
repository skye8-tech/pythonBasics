# Data analytics
# sales_data = [
#     {"Rice": [100, 1000]},
#     {"Apples": [700, 500]},
#      {"Banana": [500, 600]},
#     { "Cake": [1200, 1500]},
# ]
# category_totals = {}
# for sales in sales_data:
#   for category, amount in sales.items():
#     total = sum(amount)
#     category_totals[category] = total
# print(category_totals)


sales_data = {"Rice": [100, 1000], "Apples": [700, 500],
              "Banana": [500, 600], "Cake": [1200, 1500]}
category_totals = {}
items = sales_data.items()
print(items)
for category, amount in sales_data.items():
    total = sum(amount)
    category_totals[category] = total
print(category_totals) #print this data on a table

# |Category      |        Total Amount |
# |Rice          |       2500          |


