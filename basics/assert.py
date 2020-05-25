x = int(input("Please enter a positive integer: "))

for i in range(1, x + 1):
    if(i % 10 == 0):
        continue
    print(i)