
class Rectangle:

    def __init__(self, width, length):
        self._width = width  # protected
        self.__length = length  # private

    def getwidth(self):
        return self._width

    def setwidth(self, width):
        self._width = width

    def delwidth(self, width):
        del self._width

    width = property(getwidth, setwidth, delwidth)


rect = Rectangle(5, 6)

# print(rect._width) # protected
# print(rect._Rectangle__length) # private

# rect.setwidth(6)
# print(rect.getwidth())

rect.width = 45  # rect.setwidth(6)
print(rect.width)  # rect.getwidth()
del rect.width          # rect.delwidth()
