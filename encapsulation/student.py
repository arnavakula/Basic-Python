class Student:
    def __init__(self):
        #declare private variables with two underlines
        self.__id = 1148118
        self.__name = "Arnav"
    def display(self):
        print(self.__id)
        print(self.__name)

# s1 = Student()
# s1.display()
#name mangling - access private variables w/o a getter method
#underscore class-name underscore * 2 variable name
# print(s1._Student__id)

class Student2:
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

s2 = Student2()
s2.set_id(1148118)
s2.set_name("Arnav Akula")

print(s2.get_id())
print(s2.get_name())
    