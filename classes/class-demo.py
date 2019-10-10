
class Rectangle:

    count = 0  # class attribute

    def __init__(self, length, width):
        # instance attribtues
        self.length = length
        self.width = width
        Rectangle.count += 1

    def area(self):
        return self.length * self.width


r1 = Rectangle(4, 5)
r2 = Rectangle(6, 7)

print(r1.area())
print(r1.count)
print(r2.count)
