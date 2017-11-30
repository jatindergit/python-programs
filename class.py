class Employee:
    """This class is used to bind the data to employees"""

    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

print(help(Employee))

class Developer(Employee):
    pass

print(help(Developer))