class Product:
    
    def __init__(self):
        self.name = 'John'
        self.description = 'Very modern'
        self.price = 700
    
    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()
print(p1.name, p1.description, p1.price)
p1.display() 