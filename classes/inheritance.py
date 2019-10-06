
class Person:
    '''Person is a class with two arguments'''

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def info(self):
        '''Introduces itself'''
        print('My username is {} and password is {}'.format(
            self.username, self.password))


# person1 = Person("Rayan", "Soemize")

# # print(person1.__doc__)
# # print(Person.__doc__)
# print(person1.info.__doc__)


class Employee(Person):
    '''Employee inherits Person'''

    def __init__(self, username, password, salary):
        super().__init__(username, password)
        # Person.__init__(self, username, password) # save as above
        self.salary = salary

    def info(self):
        '''Introduces itself -- employee'''
        print(
            f'My credentials are username: {self.username}, password: {self.password}, salary: {self.salary} ')


e = Employee("One", "pass", 898856.56)

print(e.salary)
e.info()
