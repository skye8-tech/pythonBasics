def tabulateData(category_totals):
    print("Category \t | Total Amount ")
    print("______________|_____________")
    for category, total in category_totals.items():
        print(f"{category} \t\t | {total}")
        print("______________|_____________")
