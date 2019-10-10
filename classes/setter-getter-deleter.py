

class Rectangle:

    def __init__(self, width, length):
        self._width = width  # protected
        self.__length = length  # private

    @property  # in-built decorator for getter
    def width(self):
        return self._width

    @width.setter  # in-built decorator for setter
    def width(self, width):
        self._width = width

    @width.deleter  # in-built decorator for deleter
    def width(self):
        del self._width


rect = Rectangle(5, 6)

rect.width = 4545

print(rect.width)
