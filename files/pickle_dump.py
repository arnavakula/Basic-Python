import pickle
import pickle_demo

f = open("student.dat", "wb")
s = pickle_demo.Student(148118, 'Arnav Akula', 95)
pickle.dump(s, f)
f.close()