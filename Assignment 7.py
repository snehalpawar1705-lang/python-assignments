class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


# Creating object of Manager
m1 = Manager("Rahul", 30, "E101", 50000, "IT")

# Calling methods
m1.display_person()
m1.display_employee()
m1.display_manager()