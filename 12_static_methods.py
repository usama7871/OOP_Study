# ============================================
# 📚 Concept: Static Methods
# ============================================
# Static methods belong to the class itself, not to an instance of the class.
# - They do not take `self` or `cls` as the first argument.
# - They can be called without creating an instance of the class.
# - Static methods are typically used for utility functions that are related to the class 
#   but don't need to access or modify instance or class-specific data.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Converts Celsius to Fahrenheit using the formula
        # (Celsius * 9/5) + 32 = Fahrenheit
        return (c * 9/5) + 32

# Usage
temp_in_celsius = 25
temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F.")

# ============================================
# 📝 Assignment:
# - Create a class `TemperatureConverter`.
# - Define a static method `celsius_to_fahrenheit(c)` that takes Celsius as an argument 
#   and returns the corresponding Fahrenheit value.
# - Static methods are useful for operations that don't need access to the instance data.
# ============================================
 
