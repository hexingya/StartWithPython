# Recursive function


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5))

# number = int(input("Enter a numbre: "))

# number += number * 2 ** 3

# print(number)
