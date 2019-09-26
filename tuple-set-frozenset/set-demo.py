# set --- a set is an unordered collection of distinct items -- no duplicate values/items -- it cannot be indexed -- {} -- mutable/changable

# empty set
# software = set()

# len(softwares) - 6
softwares = {"Firefox", "Windows", "WhatsApp",
             "Instagram", "Photoshop", "VS Code", "VS Code"}

# print(type(softwares))
# print(softwares)
# print(len(softwares))

# to add item
# softwares.add("Facebook")

# to clear/empty set
# softwares.clear()

# to copy a set
# softwares_copy = softwares.copy()

# to remove item
# softwares.remove("Firefox")

# print(softwares_copy)

# to pop out and delete the item
# print(softwares.pop())
# print(softwares.pop())


# print(softwares)


sports = {"Cricket", "Football", "Archery",
          "Hockey", "Baseball", "Badminton", "Tennis"}
indoor = {"Badminton", "Tennis"}
outdoor = {"Cricket", "Football", "Hockey", "Baseball"}

# union
# print(indoor.union(outdoor))
# print(indoor.union(sports))

# alternative way of union operation
# union_set = indoor | outdoor

# print(union_set)

# intersection
# print(indoor.intersection(outdoor))
# print(indoor.intersection(sports))

# alternative way of intersection operation
# intersection_set = sports & outdoor

# print(intersection_set)

# Difference
# print(indoor.difference(outdoor))
# print(sports.difference(outdoor))

# alternative way of difference operation
# difference_set = sports - indoor

# print(difference_set)

# symmetric_difference
# print(indoor.symmetric_difference(outdoor))
# print(sports.symmetric_difference(outdoor))

# alternative way of symmetric_difference operation
# symmetric_difference_set = sports ^ indoor

# print(symmetric_difference_set)

# to discard set item
# sports.discard("Football")
# print(sports)
# sports.discard("Volleyball")
# print(sports)

# issubset
# print(indoor.issubset(sports))

# issuperset
# print(indoor.issuperset(sports))
# print(sports.issuperset(indoor))

# isdisjoint
# print(indoor.isdisjoint(outdoor))
# print(outdoor.isdisjoint(sports))

# update
# outdoor.update(indoor)
# print(outdoor)
# print(indoor)

# difference_update
# outdoor.difference_update(indoor)
# print(outdoor)
# print(indoor)

# symmetric_difference_update
# outdoor.symmetric_difference_update(indoor)
# print(outdoor)
# print(indoor)
