from threading import *

class MyThread(Thread):
    def run(self):
        print(current_thread().getName())
        for i in range(0, 11):
            print(i)

t = MyThread()
t.start()


