from typing import List


class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self, name):
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee):
        self.employees.append(employee)


company = Company("TechCorp")
employee1 = Employee("Alice")
company.add_employee(employee1)
