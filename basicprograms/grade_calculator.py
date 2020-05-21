m, p, c = [int(x) for x in input("Enter your math, physics, and chemistry score: ").split(', ')]
low = min(m, p, c)
avg = float((m + p + c)/3)

if low < 35:
    print("You have failed at least one exam")
else:
    if avg <= 59:
        print("You got a C average")
    elif avg <= 69:
        print("You got a B grade")
    else:
        print("You got an A grade")
        