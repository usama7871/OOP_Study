# ============================================
# 📚 Concept: self - Object Specific
# ============================================
# The 'self' keyword is used to refer to the instance of the class itself. 
# It allows you to bind attributes and methods to the object that is being created.

# Example: 
# - self allows us to define instance variables that belong to the specific object.

class Student:
    # Constructor method (__init__) which is used to initialize object-specific data.
    def __init__(self, name, marks):
        # Using self to initialize the instance variables of the object.
        # 'self.name' and 'self.marks' are unique to each instance of the Student class.
        self.name = name      # Instance-specific attribute
        self.marks = marks    # Instance-specific attribute
    
    # Instance method to display student details
    def display(self):
        # Using 'self' to access instance-specific attributes and print them
        print(f"Name: {self.name}, Marks: {self.marks}")

# Usage of the class
s1 = Student("Usama", 95)  # Creating an object 's1' of the Student class with name and marks
s1.display()  # Calling the 'display()' method to print the student's details

s2 = Student("Ali", 88)    # Creating another object 's2' of the Student class with different details
s2.display()  # Calling 'display()' for the second student

# ============================================
# 📝 Assignment:
# - Create a class `Student` with attributes `name`, `marks`.
# - Use `self` keyword to initialize attributes in the constructor.
# - Add a method `display()` that prints student details.
# ============================================
 
