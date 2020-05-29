def custom_gen(x, y):
    while x < y:
        yield x
        x += 1

result = custom_gen(20, 30)
for i in result: print(i)