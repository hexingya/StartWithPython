class Demo:
    def __init__(self, noofvisits=0):
        self.noofvisits = noofvisits

    def display(self):
        print(self.noofvisits)


y = Demo(690)
y1 = Demo(6)

print(y.noofvisits)
print(y1.noofvisits)
