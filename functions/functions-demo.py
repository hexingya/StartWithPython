# function


# def greet(name):
#     print("Hello", name)


# greet("John")
# greet("Jane")

# def add(num1, num2, num3):
#     #
#     return num1 + num2 + num3


# result = add(5, 12, 67)
# print(result)


# def greet(name="John Doe"):
#     print("Hello!", name)


# greet()
# greet("Rahul")


# def mul(a=2, b=3, c=6):
#     return a * b * c


# print(mul())
# print(mul(4, 5, 10))

# print(mul(1))


# def mul(a=2, b=3, c=6):
#     return a * b * c


# # print(mul())
# # print(mul(4, 5, 10))

# # print(mul(1))

# # print(2, 5)
# print(mul(b=2, c=5))

# def newfunction(b, c=4, a=34):
#     print(a, b, c)


# newfunction(c=5, a=56, b=38)

# def learn(lang="Python", hours=120):
#     print(lang, hours)


# learn(hours=100)

# arbitrary arguments
# def getvalues(x, y, z, *args):
#     print(args)


# getvalues(23, 3, 4)
# getvalues(23, 3, 4, 34, 56, 4545)


# def somefunction(y, x=4, *args):
#     print(y, x, args)


# # somefunction(45, 3, 4, 734, 13)
# somefunction(4, 10, 12, 23)

# def func200():
#     return [5, 56, 4545, 50, 4]

# a, b, c, d, e = func200()

# print(a, c)


# Recursive function

# import sys

# sys.setrecursionlimit(5000)


# def factorial(number):
#     if(number == 0):
#         return 1
#     else:
#         return number * factorial(number - 1)


# print(factorial(3000))

def summation(values):
    if len(values) == 1:
        return values[0]
    else:
        return values[0] + summation(values[1:])


values = (4, 1000, 3, 3, 6)
print(summation(values))
