class Student:
    def __init__(self, name, marks):
        if not name:
            raise ValueError("Missing name")
        if not marks:
            raise ValueError("Missing marks")
        self.name = name
        self.marks = marks
def main():
    student = get_student()
    print(f"{student.name} got {student.marks} marks.")

def get_student():
    name = input("Name:")
    marks = int(input("Marks:"))
    return Student(name, marks)

if __name__ == "__main__":
    main()