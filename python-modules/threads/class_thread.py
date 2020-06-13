from threading import *
from time import sleep

class MyThread:
    def display_nums(self):
        print(current_thread().getName())
        sleep(1)
        for i in range(0, 11): print(i)

obj = MyThread()
t = Thread(target = obj.display_nums)
t.start()

t2 = Thread(target = obj.display_nums)
t2.start()

t3 = Thread(target = obj.display_nums)
t3.start()

#result order is somewhat random
