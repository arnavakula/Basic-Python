a = [x for x in range(1, 6)]
b = [x for x in range(6, 11)]

prod = []
for i in range(0, len(a)):
    prod.append(a[i] * b[i])

print(prod)

prod2 = [a[i] * b[i] for i in range(0, len(a))]

print(prod2)