class ObjectCounter:
    object_number = 0

    def __init__(self):
        ObjectCounter.object_number += 1
    
    @staticmethod
    def display_count():
        print(ObjectCounter.object_number)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.display_count()

#keeping track of number of objects