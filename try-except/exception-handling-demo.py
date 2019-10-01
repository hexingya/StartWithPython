
# print(msg) # NameError

# print(7 - "apple ") # TypeError

# print(45 / 0)  # ZeroDivisionError

# handling ValueError
# try:
#     number = int(input("Enter an integer: "))
# except ValueError:
#     print('please, pass digits')

# handling TypeError

# try:
#     num = input('A Value? ')
#     print(num - 45)
# except TypeError:
#     print('operand must be integers')

# handling multiple errors

try:
    dividend = int(input("Enter an integer: "))
    divider = int(input("Enter another integer: "))

    print('Result: {}/{} = {}'.format(dividend, divider, dividend/divider))
except TypeError:
    print('Error -- type error')
except ValueError:
    print('Error -- value error')
except ZeroDivisionError:
    print('Error -- divider shouldn\'t be 0')
else:
    print("No error")
finally:
    print('Thanks')
