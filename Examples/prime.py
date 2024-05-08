# check of prime number
# xtics: it can divide just 1, and it self,

num = int(input("Enter Num: "))
count = 0
for i in range(1, int(num / 2) +1):
    if num % i == 0:
        count+=1
if count == 1:
    print(f"{num} is Prime")
else:
    print(f"{num} is not prime")