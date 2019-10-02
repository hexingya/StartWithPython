
try:
    number = 4
    print(number)
    print("*" * 3)
    print(6/0)
except TypeError:
    print('Invalid operand type')
except NameError:
    print('check whether variable is undefined')
except:
    print('Something went wrong!')
else:
    print('Okay! No error?')
finally:
    print("Just finished!")
