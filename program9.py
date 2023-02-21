# write a program to create an employee class and demonstrate inheritance in python

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display(self):
        super().display()
        print("Department:", self.department)

# create an Employee object
emp1 = Employee("John", 5000)
emp1.display()

# create a Manager object
mgr1 = Manager("Mary", 8000, "Sales")
mgr1.display()

