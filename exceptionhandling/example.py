import logging

logging.basicConfig(filename = "zerodivision.log", level = logging.DEBUG)

try:
    a, b = [int(x) for x in input("Enter two integers: ").split(',')]
    logging.info("Division in progress")
    c = a/b

except ZeroDivisionError:
    print("You cannot divide by zero")
    logging.error("ZeroDivisionError")

else:
    print("You did not divide by zero")

finally:
    print("Finally statement - code after the exception")