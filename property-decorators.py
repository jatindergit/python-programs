class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self,name):
        self.first_name, self.last_name = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Fullname deleted!')
        self.first_name = None
        self.last_name = None


emp = Employee('Jatinder', 'Singh')

emp.fullname = 'jack Denial'

emp.first_name = 'Haneet'

del emp.fullname

print(emp.first_name)
print(emp.email)
print(emp.fullname)
