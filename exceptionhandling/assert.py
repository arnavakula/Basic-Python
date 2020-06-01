exception_check = True

while(exception_check):
    try:
        num = int(input('Enter an integer: '))
        assert(num % 2 == 0), "You have entered an odd number(invalid)"
    except AssertionError as obj:
        print(obj)
    else:
        exception_check = False
    
