class InvalidPasswordException(Exception):
    def __init__(self):
        self.password = password

try: 
    password = input("Please enter a password of 8 characters: ")
    if len(password) != 8: raise InvalidPasswordException
    
except InvalidPasswordException:
    print("Your password is not 8 characters long")

else: 
    print("You entered a password of 8 characters")

