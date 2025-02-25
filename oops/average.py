class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        i=0
        for i in self.marks:
            i +=i
        print(f"Average {i/3}")

s1 = Student("David Malan",[98,97,80])
s1.get_average()