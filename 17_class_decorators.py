
# ============================================
# 📚 Concept: Class Decorators
# ============================================
# A class decorator is a function that takes a class as an argument and modifies 
# it by adding or changing methods or attributes.
# In this example, we will create a decorator that adds a new method to a class.

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"  # Adds a greet method to the class
    return cls

@add_greeting  # Applying the decorator to the class
class Person:
    def __init__(self, name):
        self.name = name

# Usage Example:
# Create an object of Person and call the greet method added by the decorator.
person = Person("Usama")
print(person.greet())  # Outputs: Hello from Decorator!

# ============================================
# 📝 Assignment:
# - Create a class decorator `add_greeting` that adds a `greet()` method to the class.
# - Apply the decorator to a class `Person` and call the `greet()` method.
# ============================================







 
