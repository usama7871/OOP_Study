# ============================================
# 📚 Concept: Instance Methods
# ============================================
# - Instance methods are functions defined inside a class that operate on instances of the class.
# - They access and modify instance variables using the `self` keyword.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()

# ============================================
# 📝 Assignment:
# - Create a class `Dog` with instance variables `name` and `breed`.
# - Add an instance method `bark()` that prints a message including the dog's name.
# ============================================
 
