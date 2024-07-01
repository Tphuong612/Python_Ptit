class BankAccount:
    def __init__(self, ac_number, balance, date_of_opening, customer_name):
        self.ac_number = ac_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name =customer_name
    def deposit(self, gtr):
        self.balance += gtr
        return self.balance
    def withdraw(self, gtr):
        self.balance -= gtr
        return self.balance
    def and_check_balance(self):
        return self.balance
    def display(self):
        return f"{self.ac_number} {self.customer_name} {self.balance}"
ac1 = BankAccount('123', 1500, '15/4/2021', 'phuong')
print(ac1.display())