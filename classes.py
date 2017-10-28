class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,  self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp1 = Employee('Toto', 'Vasile', 50000)

print (emp1.fullname())
