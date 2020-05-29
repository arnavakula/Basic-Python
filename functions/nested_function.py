def display(name):
    def message():
        return "Hello "
    result = message() + name
    return result

print(display("Arnav Akula"))

#message does not appear in global scope