# CS50P

## Description
This repository contains my solutions and notes for the CS50 Python course. I am using this space to practice coding, experiment with different approaches, and document my learning journey.

## Table of Contents
- Functions, Variables
- Conditionals
- Loops
- Exceptions
- Libraries
- Unit tests
- File I/O
- Regular Expressions
- Object Oriented Programming


## How to Use
### Clone the repository for Github Repository
[Repository](https://github.com/ujjwalbasnyat/codespace)

## Resources
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
- [Python Official Documentation](https://docs.python.org/3/)

## Contributing
Feel free to fork this repository and submit pull requests if you find better solutions or improvements!

# Python Libraries and Packages

Libraries extend the abilities of Python. Some libraries are included by default with Python and simply need to be imported. Others are third-party packages that need to be installed using `pip`. You can also create your own packages for personal use or to share with others!

# Regular expressions (Regex)

## Regex Patterns

### MetaCharacters
- **.   any character except a new line**
- **(*)   0 or more repetitions**
- **+   1 or more repetitions**
- **?   0 or 1 repetition**

### Quantifiers
- **{m} m repetitions**
- **{m,n} m-n repetitions**

### Anchors
- **^   matches the start of the string**
- **$   matches the end of the string or just before the newline at the end of the string**

### Character set and Character Classes
- **[]    set of characters**
- **[^]   complementing the set**

### PreDefined Character classes
- **\d    decimal digit**
- **\D    not a decimal digit**
- **\s    whitespace characters**
- **\S    not a whitespace character**
- **\w    word character, as well as numbers and the underscore**
- **\W    not a word character**

### Alternation
- **A|B     either A or B**

### Grouping Constructs
- **(...)   a group**
- **(?:...) non-capturing version**


# Object Oriented Programming

### Class
Class is a blueprint of template for creating objects. It define the properites(attributes) and methods inside it. Think like Class is the Architectural plan.

### Instances
An instance are the specific object created from the class. Think like Object as Proper implementation of the Architectural plan into the real world.

### constructor
```Python
# class definition
class Student:
    # default constructor
    # Class attribute (shared by all instances)
    collage_name = "ABC Collage"
    def __init__(self, name, marks):
        # Object attributes (unique to each instance)
        self.name = name
        self.marks = marks
        print("adding new student in database...")


# objects/instances
s1 = Student("David", 97)
print(s1.name, s1.marks)

s2 = Student("Marquez", 96)
print(s2.name, s2.marks) 
```

### Attributes
Attributes are the variables declared into constructor.

### Types of Attrubutes
- Class attributes
- Object attributes
- Private attributes
- Public attributes

```Python
# Private attribute is followed by underscore
def __init__(self):
    self._name = name 
# Public attribute is normal attribute no any underscore
def __init__(self):
    self.name = name 
```

### Method
Methods are the function defined inside the class.

### Types of methods
- Private method
```Python
# Same as private attribute, private methods definition is also followed by underscore
def _home(self):
    print("this is private method")
- Public method
# Public method definition does not follow any underscore
def _home(self):
    print("this is public method")
```

**Method Syntax** 

```Python

class Student():
    def __init__(self, name):
        self.name = name

    # The function Welcome is the method 
    def welcome(self): 
        print(f"Welcome {self.name}")
s1 = Student("David")
s1.Welcome()
```

### Decorator
A decorator are essentially a function that makes another function(or method) as argument and extends or modifies its behaviour.It is like wrapping a gift - the original function is gift. And the decorator is the wrapping thats adds something extra.

### Properties with decorators
Key decorators: `@property`, `@<attribute>.setter`, and `@<attribute>.deleter`.

### Code Example 
1. Method decorator

```Python
def log_call(func):
    def wrapper(self):
        print(f" Calling {func.__name__}")
        return func(self)
    return wrapper
class Person:
    def __init__(self,name):
        self.name = name
    @log_call
    def gift(self, name):
        print(f"Hello, {name} this is Gift")

p1 = Person("David")
p1.gift()
```
 

# Features of OOPS

## 1. Encapsulation
This is about bundling data (like variables) and the methods (functions) that work on that data into a single unit, usually called a class. It also involves controlling access to that data—think of it like putting a protective shield around it so only certain parts of the program can mess with it. For example, you might hide a variable and only allow changes through a specific method.

## 2. Abstraction
Hiding implementation details of a class and only showing the essential features to each user.
i.e. In the given Methods essential features is ``` print() ``` and rest of others are implementation details.

```Python
def get_average(self):
    i=0
    for i in self.marks:
        i +=i
    print(f"Average {i/3}")

```
## 3. Inheritance
Inheritance in the Oops in important concept where the class(a class called subclass or derived class) can inherit the properties and behaviours(attributes and methods) from another class(super-class or base-class).Its like a child inheriting traits from a parent except in programming, it's about resuing of code and establishing relation between classes.

### Types of Inheritance
- Single inheritance
- Multi-level inheritance
- Multiple inheritance


## 4. Polymorphism : Operator Overloading
Polymorphism is a core OOP concept that means "many forms." It’s the ability of different objects to respond to the same action (like a method call or operation) in their own unique way. Think of it like a universal remote: you press "play," and a TV, a DVD player, or a music app all play something—but each does it differently.

