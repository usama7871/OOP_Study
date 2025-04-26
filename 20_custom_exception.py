# ============================================
# 📚 Concept: Custom Exceptions
# ============================================
# Custom exceptions are user-defined exceptions in Python that allow us to raise specific error messages.
# Here, we will define a custom exception `InvalidAgeError` and raise it when the age is less than 18.

class InvalidAgeError(Exception):
    # This is our custom exception class, which inherits from the built-in Exception class
    def __init__(self, message):
        self.message = message  # Store the custom error message
        super().__init__(self.message)  # Call the base class constructor

def check_age(age):
    if age < 18:
        # Raise the custom exception if age is less than 18
        raise InvalidAgeError("Age must be 18 or older")
    else:
        print(f"Age {age} is valid.")

# Usage Example:
try:
    check_age(15)  # This will raise the custom exception
except InvalidAgeError as e:
    print(f"Error: {e}")  # Catch and print the custom error message

# ============================================
# 📝 Assignment:
# - Create a custom exception `InvalidAgeError`.
# - Raise the exception in the `check_age()` function when `age < 18`.
# - Handle the exception using `try...except`.
# ============================================
 
