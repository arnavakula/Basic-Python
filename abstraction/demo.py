from abc import *

class BMW(ABC):

    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make

    @abstractmethod
    def start(self):
       pass

    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW): #basically implements

    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(model, year, make) #inherit reusable properties (w/o self)
        self.cruiseControlEnabled = cruiseControlEnabled

    def start(self): #Overriding
        print("Starting the Three Series")
    
    def stop(self):
        print("Stopping the Three Series")
    
    def drive(self):
        print("Driving Three Series")

class FiveSeries(BMW): #instead of extends

    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, model, year, make) #inherit reusable properties using parent class explicitly
        self.parkingAssistEnabled = parkingAssistEnabled
    
    def start(self): #Overriding
        print("Starting the Five Series")
    
    def stop(self):
        print("Stopping the Three Series")
    
    def drive(self):
        print("Driving Five Series")

three_series = ThreeSeries(True, "BMW", "328i", 2018)
five_series = FiveSeries(True, "BMW", "530i", 2019)

print(three_series.cruiseControlEnabled)
print(five_series.parkingAssistEnabled)

three_series.start()
three_series.stop()
three_series.drive()
five_series.drive()

#cannot instantiate abstract class


