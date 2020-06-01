try:
    f = open("myfile.txt", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split(',')]
    c = a/b
    f.write("Writing %d into file" %c)
except ZeroDivisionError:
    print("You cannot divide by zero")
else: #if there is no exception
    print("You did not divide by zero")
finally: #must be done
    f.close()
    print("File closed")
print("Code after exception")
