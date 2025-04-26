# ============================================
# 📚 Concept: Aggregation
# ============================================
# Aggregation is a type of relationship between objects where one object contains 
# a reference to another object, but the referenced object can exist independently.
# This is a "has-a" relationship, but in contrast to composition, 
# the contained objects do not necessarily depend on the life cycle of the parent object.
# In aggregation, the child object (in this case, the Employee) can exist outside the context 
# of the parent object (the Department).

class Employee:
    def __init__(self, name, position):
        """
        Constructor for Employee class. This class represents an employee with a name and position.

        Args:
            name (str): Name of the employee.
            position (str): Position of the employee.
        """
        self.name = name
        self.position = position

    def display(self):
        """
        Method to display the employee's details.
        """
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, dept_name):
        """
        Constructor for Department class. The department will store references to employee objects.

        Args:
            dept_name (str): Name of the department.
        """
        self.dept_name = dept_name
        self.employees = []  # List to store employees associated with the department

    def add_employee(self, employee):
        """
        Add an Employee object to the department. This shows aggregation, as the Employee 
        exists independently from the Department.

        Args:
            employee (Employee): The Employee object to be added to the department.
        """
        self.employees.append(employee)

    def display_employees(self):
        """
        Method to display all employees in the department.
        """
        print(f"Employees in {self.dept_name} Department:")
        for emp in self.employees:
            emp.display()

# Usage Example:
# Create employee instances.
emp1 = Employee("Alice", "Software Developer")
emp2 = Employee("Bob", "Data Scientist")

# Create department instance.
dept = Department("Tech")

# Add employees to the department.
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display all employees in the department.
dept.display_employees()
 
