class Student:
    major = "CSE"

    def __init__(self, id, name):
        self.name = name
        self.id = id
    
s1 = Student(1148118, "Arnav Akula")
print(s1.major)
print(Student.major)
