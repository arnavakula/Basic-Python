import os, sys

if os.path.isfile('testfile.txt'):
    f = open('testfile.txt', 'r')
else: 
    print("File does not exist")
    sys.exit()

s = f.read()
print(s)
f.close()
