
class Person:

    def __init__(self, name, age=100, *args, **kwargs):
        self.name = name
        self.age = age
        self.restvalues = args
        self.otherrestvalues = kwargs

    def greet(self):
        print(f'Hello {self.name}! you are {self.age} year\'s old.')
        print(self.restvalues)
        print(self.otherrestvalues)


p = Person("Jane")
p2 = Person("Laxmi", 1, 4, 545, 5665, 900, a=4, b=34, c=0)

p.greet()
p.name = "Joya"
p.age = 2
print(p.name)
print(p.age)

print(p2.name)
p2.greet()
