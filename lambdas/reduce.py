from functools import *

lst = [5, 10, 15, 20]
res = reduce(lambda x, y: x + y, lst)
print(res)