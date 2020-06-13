from threading import *

class EvenNumbersThread:
    def count(self):
        for i in range(0, 101, 2):
            print(i)

class OddNumbersThread:
    def count(self):
        for i in range(1, 101, 2):
            print(i)

e = EvenNumbersThread()
t_even = Thread(target = e.count)
o = OddNumbersThread()
t_odd = Thread(target = o.count)

for i in range(0, 100): print(i)
t_even.start()
t_odd.start()
