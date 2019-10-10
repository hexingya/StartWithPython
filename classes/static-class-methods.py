
class Rectangle(object):

    count = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width
        Rectangle.count += 1

    def area(self):
        return self.length * self.width

    @classmethod
    def info(cls):
        return cls.count  # Rectangle.count

    @staticmethod
    def important(name):
        return f'hello {name}'


rect1 = Rectangle(5, 7)
rect2 = Rectangle(5, 7)

print(Rectangle.info())
print(rect1.info())

print(Rectangle.important('John'))
