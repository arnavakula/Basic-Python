class BMW:

    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(model, year, make) #inherit reusable properties (w/o self)
        self.cruiseControlEnabled = cruiseControlEnabled

    def start(self): #Overriding
        super().start()
        print("Starting the Three Series")

class FiveSeries(BMW): #instead of extends

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, model, year, make) #inherit reusable properties using parent class explicitly
        self.parkingAssistEnabled = parkingAssistEnabled

three_series = ThreeSeries(True, "BMW", "328i", 2018)
five_series = FiveSeries(True, "BMW", "530i", 2019)

print(three_series.cruiseControlEnabled)
print(five_series.parkingAssistEnabled)

three_series.start()
three_series.stop()

