# ============================================
# 📚 Concept: Static Variables and Static Methods
# ============================================
# Static methods do not require access to any instance or class variables.
# They behave like regular functions, but are bound to the class's namespace.

class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b  # Return the sum of a and b

# Usage
result = MathUtils.add(5, 3)  # Call static method without needing an instance
print(f"Sum: {result}")  # Output: Sum: 8

# ============================================
# 📝 Assignment:
# - Create a class `MathUtils` with a static method `add(a, b)`
# - The method should return the sum of `a` and `b` without using class or instance variables
# ============================================
 
