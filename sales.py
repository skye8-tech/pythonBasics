sales_data = {"bamenda": [100, 500, 600], "Buea": [120, 260, 700], "Douala": [690, 98,9]}
# loop through key value pair, sum the values

# Bamenda: 1200
# Buea: 1080

analysed_sales = {} # is the new anayl

for town, sales in sales_data.items():
    totalSales = sum(sales)
    analysed_sales[town] = totalSales # add it to the analysed sales dictionary.

print(sales_data)
print(analysed_sales.values())