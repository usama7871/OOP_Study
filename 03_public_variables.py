# ============================================
# 📚 Concept: Public Variables and Methods
# ============================================
# Public variables and methods are accessible from outside the class. 
# They are not restricted, meaning they can be freely modified or called.

class Car:
    # Public variable to store the brand of the car
    brand = "Toyota"
    
    # Public method to start the car
    def start(self):
        print(f"The {self.brand} car is now starting.")

# Usage
car1 = Car()  # Create an instance of the Car class
print(car1.brand)  # Accessing public variable 'brand'
car1.start()  # Calling the public method 'start'

# ============================================
# 📝 Assignment:
# - Create a class `Car`
# - Use a public variable `brand` to store the car's brand
# - Use a public method `start()` to simulate starting the car
# ============================================
 
