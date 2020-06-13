#using boolean flags
from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products = []
        self.orders_placed = False #boolean flag to communicate 

    def produce(self):
        for i in range(1, 5):
            prod = "Product" + str(i)
            self.products.append(prod)
            sleep(1)
            print("Item added")
        self.orders_placed = True

class Consumer:
    def __init__(self, prod):
        self.prod = prod #producer object
    
    def consume(self):
        while(not self.prod.orders_placed):
            sleep(0.2)
        print("Orders have been placed:", self.prod.products)

p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t1.start()
t2 = Thread(target = c.consume)
t2.start()


