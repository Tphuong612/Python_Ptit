class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
    def change_depart(self, gtr):
        self.department = gtr
        return self.department
    def calculate_salary(self, salary)
    def display(self):
        print(f"{self.id} {self.name} {self.department} {self.calculate_salary()}")