from threading import *

class BookMyBus:

    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.l = Semaphore() #OR self.l = Lock()

    def buy(self, requested_seats):
        self.l.acquire()
        print("Seats available:", self.available_seats)
        if(self.available_seats >= requested_seats):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.available_seats -= requested_seats
        else:
            print("Sorry, there aren't that many seats available")
        self.l.release()

obj = BookMyBus(10)       
t1 = Thread(target = obj.buy, args = (3,))
t1.start()
t2 = Thread(target = obj.buy, args = (4,))
t2.start()
t3 = Thread(target = obj.buy, args = (4,))
t3.start()
