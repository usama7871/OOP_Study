# ============================================
# 📚 Concept: Abstract Classes and Methods
# ============================================
# - Abstract classes cannot be instantiated directly.
# - Abstract methods must be implemented in derived classes.
# - Use the `abc` module to define abstract classes and methods.

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Usage
rectangle = Rectangle(5, 10)
print(f"Area of Rectangle: {rectangle.area()}")

# ============================================
# 📝 Assignment:
# - Create an abstract class `Shape` with an abstract method `area()`.
# - Inherit a class `Rectangle` from `Shape` and implement the `area()` method.
# - Ensure that `Rectangle` calculates and returns the area.
# ============================================
 
