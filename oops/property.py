class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print("Fetching the name...")
        return self._name
    @name.setter
    def name(self, value):
        print("Changing the name...")
        if not value:
            raise ValueError("Name can;t be empty.")
        self._name = value
std1 = Student("David")
print(std1.name)
std1.name = "Mahadev"
print(std1.name)