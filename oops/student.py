# class definition
class Student():
    # default constructor
    collage_name = "ABC Collage"  #class attribute
    def __init__(self, name, marks):
        self.name = name #class attribute
        self.marks = marks #class attribute
        print("adding new student in database...")

    # paramaterized constructor

# objects/instances
s1 = Student("David", 97)
print(s1.name, s1.marks)

s2 = Student("Marquez", 96)
print(s2.name, s2.marks)

# attributes are the variables declared into constructor

# methods
# methods are the function defined inside the class