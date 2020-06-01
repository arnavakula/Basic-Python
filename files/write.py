f = open("testfile.txt", "w")
print('Type pound when you are done')
s = ''
while s != '#':
    s = input("Enter text to append: ")
    f.write(s + "\n")
    f.close