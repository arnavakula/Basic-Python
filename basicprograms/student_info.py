id = int(input("What is the student id#? "))
name = str(input("What is the student's name? "))
grade = float(input("What is the student's grade? "))

name = name[0].upper() + name[1:].lower()

print("Student id: #%i" %id)
print("Student name: %s" %name)
print("Student grade: %.1f" %grade)