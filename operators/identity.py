# Identity Operators  --- used to objects on the basis of memory location
#
# is --- return True, if objects(operands) are same (the same memory location)
#
# not is --- return False, if objects(operands) are not same (not same memory location)

# message1 = "Something"
# message2 = "Nothing"
# message3 = "Everything"
# message = "Something"

# result = message1 is message2
# print(result)
# result = message1 is message3
# print(result)
# result = message2 is message3
# print(result)
# result = message1 is message
# print(result)

# print(id(message3), id(message2))  # not same memory location
# print(id(message), id(message1))  # same memory location


x = 256
y = 10

print(id(x))
print(id(y))
print(x is y)
print(x is not 200)
