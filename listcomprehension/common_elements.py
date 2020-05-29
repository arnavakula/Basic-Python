a = [x for x in range(2, 9, 2)]
b = [i for i in range(1, 5)]

res = []
for i in a:
    if i in b:
        res.append(i)
print(res)

res2 = [x for x in a if x in b]
print(res2)