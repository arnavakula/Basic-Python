x, y = [int(i) for i in input("Enter x and y where x < y: ").split(', ')]
 
while(x < y):
    if(x % 2 != 0):
        print(x)
        x+= 2
    else: 
        x += 1