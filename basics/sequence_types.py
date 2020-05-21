#lists - can be modified
lst = [1]
print(lst)
lst1 = [10, 10.5, "String", 40]

lst1.append(59)
lst1.remove(10)
del(lst1[0])


print(max(lst1)), min(lst1)
lst1.sort(reverse = True)
lst1.insert(2, 74)
print(lst1)

#tuple - cannot be modified
tpl = (40, 50, 40, "XYZ")
print(tpl.index("XYZ"))

#conversion
lst1 = list(tpl)
tpl1 = tuple(lst1)

#sets - omits duplicates, no indexing/splicing
s = {1, 2, 2, "XYZ"}
s.update([14, 2.5])
s.remove(2)
print(s)
fs = frozenset(s)

#range - non-inclusive set of numbers
r = range(1, 16, 2)
for i in r:
     print(i)

#bytes/arrays
lst = [20, 30, 40, 234]
b = bytes(lst)
ba = bytearray(lst)
ba[3] = 29

#dictionary - key + value (no certain type for each) w/o indexing
dict1 = {1: "John", 2:"Bob"}
print(dict1)
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1[1])
del(dict1[1])

