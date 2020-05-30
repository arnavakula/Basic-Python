class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings
    
    def average(self):
        num_ratings = len(self.ratings)
        avg = (sum(self.ratings))/num_ratings
        return avg

c1 = Course('Python course', [1, 2, 3, 4, 5])
c2 = Course('Java course', [1, 2, 3, 3, 5, 5])

print(c1.name, c1.ratings)
print(c1.average(), c2.average())