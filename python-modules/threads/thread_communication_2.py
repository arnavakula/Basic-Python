#uses wait/notify
from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products = []
        self.c = Condition()
         
    def produce(self):
        self.c.acquire()
        for i in range(1, 5):
            prod = "Product" + str(i)
            self.products.append(prod)
            sleep(1)
            print("Item added")
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self, prod):
        self.prod = prod #producer object
    
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout = 0)
        self.prod.c.release()

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t1.start()
t2 = Thread(target = c.consume)
t2.start()



