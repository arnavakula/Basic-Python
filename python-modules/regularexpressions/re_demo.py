import re

str = 'Take up 12 one idea at a 23 time, one 45 idea 21-06-2001 at a time'
res = re.search(r'o\w+', str) 
print(res.group())

res = re.findall(r'o\w?', str)
print(res)

res = re.match(r'T\w{1, 2}', str)
#print(res.group())

res = re.split(r'\s\d+\s', str)
print(res)

res = re.sub(r'one', 'two', str)
print(res)

date = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(date)

res = re.findall(r'^o\w?', str)
print(res)

'''
^ uses the beginning of the string
\ signifies escape use a special character
. matches all characteres but new line
^ at beginning
$ at end
[a - b] range 
[^a-b] everything but a-b
(matching regex)
(a|b) two regexo
'''

'''
\w signifies alphanumeric value
\d signifies digit
\s signifies whitespace
\b signifies space around words
\A start of string
\Z end of string
'''

'''
+ signifies ≥1
* signifies ≥0
? signifies 0=1
{m} signifies m times
{m, n} signifies ≥m, ≤n
'''