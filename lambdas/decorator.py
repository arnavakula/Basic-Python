#modifies a parameter function and returns it


def decor(fun):
    def inner():
        result = fun()
        return result * 2
    return inner

@decor
def get_num():
   num = int(input("Enter a number: "))
   return num

print(get_num())