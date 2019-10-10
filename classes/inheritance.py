
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return str((self.length, self.width))


class Square(Rectangle):

    def __init__(self, length, width, side):
        super().__init__(length, width)
        self.side = side

    def area(self):
        return self.side ** 2

    def __str__(self):
        return str(self.side)


sq = Square(5, 6, 50)

print(sq.length, sq.width, sq.side)
# print(sq.area())
print(sq)
