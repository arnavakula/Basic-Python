def display():
    def message():
        return "Hello"
    return message

print(display()())

#display returns a message, which we must invoke