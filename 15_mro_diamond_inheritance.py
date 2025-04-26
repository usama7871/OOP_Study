# ============================================
# 📝 Assignment:
# - Create a class `Department` that holds references to `Employee` objects.
# - The `Employee` objects should be able to exist independently of the `Department`.
# - The relationship here is aggregation, as the employee's existence is independent of the department.
# ============================================

# ============================================
# 📚 Concept: Method Resolution Order (MRO) and Diamond Inheritance
# ============================================
# Method Resolution Order (MRO) defines the order in which classes are checked 
# for methods and attributes during inheritance. In the case of diamond inheritance,
# MRO determines which class method is called first when multiple inheritance is involved.

class A:
    def show(self):
        """
        Method in class A, which is overridden by classes B and C.
        """
        print("Method in class A")

class B(A):
    def show(self):
        """
        Method in class B, overriding the method in A.
        """
        print("Method in class B")

class C(A):
    def show(self):
        """
        Method in class C, overriding the method in A.
        """
        print("Method in class C")

class D(B, C):
    def show(self):
        """
        Method in class D, which will demonstrate MRO.
        """
        print("Method in class D")

# Usage Example:
# Create an object of class D, which inherits from both B and C.
d = D()
d.show()  # This will demonstrate the MRO (Method Resolution Order).

# In this case, due to MRO, it will call the method from class B first, then class C.

# ============================================
# 📝 Assignment:
# - Create a class `A` with a method `show()`.
# - Create two classes `B` and `C` that inherit from `A` and override `show()`.
# - Create a class `D` that inherits from both `B` and `C`, and override `show()`.
# - Call the `show()` method on an instance of class `D` to observe the MRO and diamond inheritance.
# ============================================ 
