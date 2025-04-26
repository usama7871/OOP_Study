# ============================================
# 📚 Concept: `callable()` and `__call__()`
# ============================================
# `callable()` is a built-in function that checks if an object appears callable (i.e., if it can be called like a function).
# `__call__()` is a special method in Python that allows an instance of a class to be called as if it were a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplier factor

    def __call__(self, number):
        # The __call__ method allows the object to be used like a function
        return number * self.factor

# Usage Example:
multiplier = Multiplier(5)
print(callable(multiplier))  # Outputs: True (because of __call__ method)

result = multiplier(10)  # Calling the object like a function
print(result)  # Outputs:
 
