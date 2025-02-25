class Student():
    collage_name = "ABC Collage"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database...")

s1 = Student("David", 97)
print(s1.name, s1.marks)

s2 = Student("Marquez", 96)
print(s2.name, s2.marks)