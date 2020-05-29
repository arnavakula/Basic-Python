def decor(fun):
    def inner(name):
        result = fun(name) + ", how are you?"
        return result
    return inner

@decor
def hello(name):
    return ("Hello " + name)

print(hello("Arnav"))