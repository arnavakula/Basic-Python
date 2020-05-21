x = int(input("Enter an integer: "))

if(x == 0):
    print("0 is neither even nor odd")
elif(x % 2 == 0):
    print(x, "is even.")
else:
    print(x, "is odd.")

