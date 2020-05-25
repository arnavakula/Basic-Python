primeFlag = True
num = int(input("Please enter a positive integer: "))

for i in range(2, int((num / 2) + 2)):
    if(num % i == 0):
        primeFlag = False
        break

if(primeFlag):
    print(num, "is prime")
else:
    print(num, "isn't prime")