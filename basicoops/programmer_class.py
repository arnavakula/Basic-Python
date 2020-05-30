class Programmer:

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def set_technologies(self, technologies):
        self.technologies = technologies
    
    def get_technologies(self):
        return self.technologies

p1 = Programmer()
p1.set_name("Arnav Akula")
p1.set_salary(100000)
p1.set_technologies(['Java', 'Python', 'C++'])

print(p1.get_name())
print(p1.get_salary())
print(p1.get_technologies())