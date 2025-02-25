def log_call(func):
    def wrapper(self):
        print(f" Calling {func.__name__}")
        return func(self)
    return wrapper

class Person:
    def __init__(self,name):
        self.name = name

    @log_call
    def gift(self):
        print(f"Hello{self.name}, this is Gift")

p1 = Person("David")
p1.gift()