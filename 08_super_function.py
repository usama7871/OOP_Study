# ============================================
# 📚 Concept: The `super()` Function
# ============================================
# - `super()` is used to call a method from the parent class.
# - Commonly used in constructors to initialize attributes from the base class.

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # Calling the constructor of the base class (Person)
        super().__init__(name)
        self.subject = subject

    def display(self):
        # Call the display method of the base class using super()
        super().display()
        print(f"Subject: {self.subject}")

# Usage
teacher = Teacher("Usama", "Mathematics")
teacher.display()

# ============================================
# 📝 Assignment:
# - Create a class `Person` with a constructor to set the `name`.
# - Inherit a class `Teacher` from `Person`, add a `subject` field.
# - Use `super()` in `Teacher` to call the constructor of `Person` and initialize `name`.
# ============================================
 
