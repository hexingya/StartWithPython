class Rectangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return str((self.length, self.width))

    def __add__(self, obj):
        return Rectangle(self.length + obj.length, self.width + obj.width)

    def __mul__(self, obj):
        return Rectangle(self.length * obj.length, self.width * obj.width)

    def area(self):
        return self.length * self.width


rec1 = Rectangle(6, 7)
rec2 = Rectangle(3, 1)

print(Rectangle.area(rec2))
print(rec2.area())

print(rec1)
print(rec2)
print(rec1 + rec2)  # rec1.__add__(rec2)
print(rec1 * rec2)  # rec1.__mul__(rec2)
