class Patient:
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
        
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_ssn(self, ssn):
        self.ssn = ssn

    def get_ssn(self):
        return self.ssn

p1 = Patient()
p1.set_id(12345)
p1.set_name("Jack")
p1.set_ssn(123456789)

print(p1.get_id())
print(p1.get_name())
print(p1.get_ssn())