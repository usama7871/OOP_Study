# ============================================
# 📚 Concept: Property Decorators
# ============================================
# Property decorators are used to control access to instance attributes.
# They provide a clean way to use getter, setter, and deleter methods as properties.
# Here, we will define a property for the `price` attribute of the `Product` class.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute to store price

    @property
    def price(self):
        # This is the getter, which allows reading the price attribute
        return self._price

    @price.setter
    def price(self, value):
        # This is the setter, which allows updating the price attribute
        if value > 0:
            self._price = value
        else:
            print("Price must be greater than 0")

    @price.deleter
    def price(self):
        # This is the deleter, which allows deleting the price attribute
        print("Price is being deleted")
        del self._price

# Usage Example:
product = Product(100)
print(product.price)  # Outputs: 100

product.price = 120  # Updates price
print(product.price)  # Outputs: 120

del product.price  # Deletes price

# ============================================
# 📝 Assignment:
# - Create a class `Product` with a private attribute `_price`.
# - Use `@property` for the getter, `@price.setter` for the setter, and `@price.deleter` for the deleter.
# ============================================
 
