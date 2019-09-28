# Logical Operators
#
# and -- returns true, if both operands are true
# or    -- returns true, if one of operands is true
# not   -- reverse the result (true into fasle and vice versa)
#

yes = True
no = False

# print(type(no))

# and
# print(yes and no)  # False
# print(yes and True)  # True
# print(yes and False)  # False

# or
# print(yes or no)  # True
# print(yes or True)  # True
# print(yes or False)  # True
# print(no or no)  # False

# not
# print(not yes)  # False
# print(not not False)  # False

price = int(input('Enter price: '))
balace = 8000

purchasing_condition = price <= balace
nope_condition = balace < price

print(purchasing_condition and not nope_condition)
print(purchasing_condition or nope_condition)
print(not purchasing_condition)
