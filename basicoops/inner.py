class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    class Engine:
        def __init__(self, num):
            self.num = num
        def start(self):
            print("Engine has started")

car = Car("BMW", 2017)
eng = car.Engine(123)

eng.start()
