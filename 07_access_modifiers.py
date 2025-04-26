# ============================================
# 📚 Concept: Access Modifiers: Public, Private, and Protected
# ============================================
# - Public: Accessible from anywhere
# - Protected: Intended for internal use, but accessible outside the class
# - Private: Not directly accessible outside the class (name mangled)

class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        # Protected variable (convention: single underscore)
        self._salary = salary
        # Private variable (name mangled with double underscores)
        self.__ssn = ssn

    def display(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

# Usage
emp = Employee("Usama", 50000, "123-45-6789")

# Accessing public variable
print(emp.name)  # Accessible

# Accessing protected variable (not recommended, but works)
print(emp._salary)  # Accessible, but should be considered internal

# Accessing private variable (will raise an error)
# print(emp.__ssn)  # AttributeError: 'Employee' object has no attribute '__ssn'

# To access the private variable, we can use name mangling
print(emp._Employee__ssn)  # Accessing private variable through name mangling

# ============================================
# 📝 Assignment:
# - Create a class `Employee` with:
#   - a public variable `name`
#   - a protected variable `_salary`
#   - a private variable `__ssn`
# - Try accessing all three variables from outside the class and observe what happens
# ============================================
 
