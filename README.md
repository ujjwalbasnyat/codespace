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
- Et Cetera

## Course topic covered
- Functions, Variables
- Conditionals
- Loops
- Exceptions
- Libraries
- Unit tests
- File I/O
- Regular Expressions

## How to Use
### Clone the repository for Github Repository
[Repository](https://github.com/ujjwalbasnyat/codespace)

## Resources
- [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/)
- [Python Official Documentation](https://docs.python.org/3/)

## Contributing
Feel free to fork this repository and submit pull requests if you find better solutions or improvements!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



# Python Libraries and Packages

Libraries extend the abilities of Python. Some libraries are included by default with Python and simply need to be imported. Others are third-party packages that need to be installed using `pip`. You can also create your own packages for personal use or to share with others!

## Topics Covered

- **Libraries**
- **Random**
- **Statistics**
- **Command-Line Arguments**
- **Slice**
- **Packages**
- **APIs**
- **Making Your Own Libraries**

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
```

### Attributes
attributes are the variables declared into constructor.

### Types of Attrubutes
- Class Attributes
- Object Attributes

### Method
Methods are the function defined inside the class.

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

## Static Methods

### Decorator

# Features of OOPS

**1. Encapsulation**
This is about bundling data (like variables) and the methods (functions) that work on that data into a single unit, usually called a class. It also involves controlling access to that data—think of it like putting a protective shield around it so only certain parts of the program can mess with it. For example, you might hide a variable and only allow changes through a specific method.

**2. Abstraction**
Hiding implementation details of a class and only showing the essential features to each user.
i.e. In the given Methods essential features is ``` print() ``` and rest of others are implementation details.

```Python
def get_average(self):
    i=0
    for i in self.marks:
        i +=i
    print(f"Average {i/3}")

```

