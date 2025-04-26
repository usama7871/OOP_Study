# ============================================
# 📚 Concept: Class Variables and Class Methods
# ============================================
# Class variables are shared across all instances of the class.
# Class methods operate on class variables and can be accessed using the class itself.

class Bank:
    # Class variable that is shared by all instances
    bank_name = "Global Bank"
    
    # Class method that modifies the class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Modify the class variable using 'cls'

# Usage
print(f"Before change: {Bank.bank_name}")  # Accessing class variable before change

# Change the bank name using the class method
Bank.change_bank_name("United Bank")
print(f"After change: {Bank.bank_name}")  # Accessing class variable after change

# Create instances of the Bank class
bank1 = Bank()
bank2 = Bank()

# Show that all instances reflect the updated bank name
print(f"Bank 1 Name: {bank1.bank_name}")
print(f"Bank 2 Name: {bank2.bank_name}")

# ============================================
# 📝 Assignment:
# - Create a class `Bank` with a class variable `bank_name`
# - Add a class method `change_bank_name(cls, name)` to modify the class variable
# - Demonstrate that the change affects all instances of the class
# ============================================
 
