# ============================================
# 📚 Concept: Composition
# ============================================
# Composition refers to the design principle where one class contains objects 
# of other classes as instance variables. It is a "has-a" relationship, 
# meaning the containing class has an instance of another class as one of its attributes.

class Engine:
    def start(self):
        # This method simulates starting the engine
        print("Engine started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        # Car uses Engine's start method via composition
        print(f"{self.brand} car is starting...")
        self.engine.start()

# Usage
engine = Engine()
car = Car("Toyota", engine)
car.start_car()

# ============================================
# 📝 Assignment:
# - Create a class `Engine` with a method `start()` that simulates starting the engine.
# - Create a class `Car` that contains an `Engine` object. This represents composition where the Car "has-a" Engine.
# - In the `Car` class, define a method `start_car()` that calls the `start()` method of the Engine object.
# ============================================
 
