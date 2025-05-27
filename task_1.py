class Employee:

  raise_amt = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  def fullname(self):
    return f'{self.first} {self.last}'

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

  raise_amt = 1.1

emp1 = Employee('Ivan', 'Ivanov', 50000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

dev1 = Developer('Petr', 'Petrov', 50000)
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

