
# ============================================
# 📚 Concept: Making a Custom Class Iterable
# ============================================
# An iterable object can be used in a for-loop and must implement two methods: `__iter__()` and `__next__()`.
# We will create a `Countdown` class that counts down to 0 from a given start number.

class Countdown:
    def __init__(self, start):
        self.start = start  # Store the starting number

    def __iter__(self):
        # The `__iter__()` method returns the iterator object
        self.current = self.start  # Initialize the current value
        return self

    def __next__(self):
        # The `__next__()` method is called each time in the for-loop
        if self.current <= 0:
            # Stop iteration once we reach 0 or below
            raise StopIteration
        else:
            self.current -= 1  # Decrement the counter
            return self.current  # Return the current value

# Usage Example:
countdown = Countdown(5)
for number in countdown:
    print(number)  # Outputs: 4, 3, 2, 1 (counting down from 5 to 1)

# ============================================
# 📝 Assignment:
# - Create a class `Countdown` that is iterable.
# - Implement `__iter__()` and `__next__()` to count down to 0.
# - Use the class in a for-loop.
# ============================================
 
