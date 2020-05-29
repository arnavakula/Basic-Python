lst = [10, 2, 33, 25, 89, 2]
lambda x:x % 2 == 0

res = filter(lambda x:x % 2 == 0, lst) #returns a filter object - type cast
print(list(res))