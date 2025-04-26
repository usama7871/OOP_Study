# ============================================
# 📚 Concept: Constructors and Destructors
# ============================================
# The constructor is called when an object is created. 
# The destructor is called when an object is destroyed (typically when it's no longer in use).

class Logger:
    # Constructor (__init__) - called when an object is created
    def __init__(self):
        print("Logger object created!")

    # Destructor (__del__) - called when the object is destroyed
    def __del__(self):
        print("Logger object destroyed!")

# Usage
log = Logger()  # This triggers the constructor and prints the creation message
del log         # Explicitly deleting the object to trigger the destructor (in practice, the destructor is often triggered automatically when an object goes out of scope)

# ============================================
# 📝 Assignment:
# - Create a class `Logger`
# - Constructor should print "Logger object created!"
# - Destructor should print "Logger object destroyed!" when the object is destroyed
# ============================================
 
