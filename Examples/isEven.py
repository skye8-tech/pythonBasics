def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


num = int(input("enter number:"))
if isEven(num):
  print("number is even")
else:
  print("num is not even")