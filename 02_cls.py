# ============================================
# 📚 Concept: cls - Class Method
# ============================================
# The 'cls' keyword is used in class methods to refer to the class itself, not the instance.
# It allows you to manipulate class-level attributes and methods.

class Counter:
    # Class variable to keep track of the number of objects created
    count = 0
    
    def __init__(self):
        # Increment the count each time an object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Using 'cls' to access the class-level variable
        print(f"Objects created: {cls.count}")

# Usage
c1 = Counter()  # Creating first object
c2 = Counter()  # Creating second object
Counter.display_count()  # Displaying the total count of created objects

# ============================================
# 📝 Assignment:
# - Create a class `Counter`
# - Use a class variable `count` to track the number of objects created
# - Add a class method `display_count(cls)` to display the number of objects
# ============================================
 
