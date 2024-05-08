dictionary = {"name": "andrew"}
sales = {"bamenda": [100, "199"]}
# Syntax Error, KeyError, AttributeError, IOError, ZeroDivisionError, ModuleNotFound, ValueError
try:
    print(dictionary["name"])
    sumOfSales = sum(sales.values())
    print(sumOfSales)
    quotient = 5 / 0
    print(quotient)
except TypeError:
    print("Can not sum int and list/string")
except KeyError:
    print("the key age does not exist")
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except IndentationError:
    print("Syntax error")

finally:
    print("Executiiono finished")