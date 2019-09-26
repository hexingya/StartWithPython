# frozenset --- like set(distinct unordered collection of items) but immutable/(not changable)

fruits = frozenset({"Apple", "Orange", "Guava", "Pineapple", "Mango"})

otherfruits = frozenset(["mango", "Guava", "Papaya"])

# print(type(fruits))

# print(fruits.difference(otherfruits))
print(fruits - otherfruits)

# practice rest of methods
