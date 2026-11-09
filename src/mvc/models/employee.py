from dataclasses import dataclass
from datetime import date 

class Employee:
    def __init__(self, employeeID: int, lastName: str, firstName: str, birthDate: date, hireDate: date):
        self.employeeID = employeeID
        self.lastName = lastName
        self.firstName = firstName
        self.birthDate = birthDate
        self.hireDate = hireDate


    