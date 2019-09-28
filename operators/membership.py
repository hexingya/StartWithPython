# Membership Operators
#
#   in --  Returns True if a sequence with the specified value is present in the object
#   not in  -- Returns True if a sequence with the specified value is not present in the object
#

# print("come" in "Welcome")
# print(45 in [34, 45, 74, 4])
# print(5 not in (34, 45, 74, 4))

# print("T" in {"O": "one", "T": "Three"})

orders = {"O": "One", "T": "Three"}

print("T" in orders.keys())
print("One" in orders.values())
print(("O", "One") in orders.items())
print(("O", "end") in orders.items())
