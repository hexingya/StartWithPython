
def decorator_greet(func):
    def wrapper_func(name):
        return 'Hello ' + func(name)
    return wrapper_func


@decorator_greet
def greet(name):
    return name


# deco = decorator_greet(greet)
# print(deco('Jane'))

print(greet("John"))
