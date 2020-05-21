#string writing, splicing, stripping
s = "  You ar e awesome"
print(s, type(s))
s1 = """You
are awesome """
print(s1)

print(s[0])
print(s * 2)
print(len(s))
print(s[0:5])
print(s[:8])
print(s[8:])
print(s[-10:-1])
print(s[::-1])

print(s.strip())

print(s.find("awe", 0, 8))
print(s.find("awe", 0, len(s)))
print(s.count("a"))
print(s.replace("awesome", "super"))
