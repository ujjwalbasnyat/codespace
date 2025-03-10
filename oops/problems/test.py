class Person:
    def __init__(self, name="David"):
        self.name = name
    
    @property
    def capacity(self):
        print("getting name...")
        return self.name

person = Person()
print(person.capacity)