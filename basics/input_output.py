import sys
#print statement
print("The second part \nwill come on a new line")

a,b = 10, 20
print(a, b)

name = "John"
grade = 94.5
print("Name is %s, grade is %.1f" %(name, grade))
print("Name is {}, grade is {}".format(name, grade))

#input
# s = input("What is your name? ")
# i = int(input("Enter an integer: "))

#multiple inputs
lst = [int(x) for x in input("Enter three numbers: ").split(', ')]
print(lst)
print(lst)