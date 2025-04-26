# ============================================
# 📚 Concept: Function Decorators
# ============================================
# A function decorator is a function that takes another function as an argument 
# and returns a new function that adds functionality to the original function.
# In this case, we are creating a decorator that logs when a function is called.

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call  # Applying the decorator to the function
def say_hello():
    print("Hello!")

# Usage Example:
# Calling the decorated function will first print "Function is being called"
# before printing "Hello!"
say_hello()

# ============================================
# 📝 Assignment:
# - Create a decorator `log_function_call` that prints a message before calling the function.
# - Apply the decorator to the `say_hello` function.
# ============================================
 
