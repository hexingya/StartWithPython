# tuple --- A tuple is a sequence like list but it is immutable(not changable)

# List -- editable/mutable
# students_list = ["John", "Jordan", "Laxmi", "Jane"]
# print(students_list[3])

students_tuple = ("John", "Jane", "Jordan", "Laxmi",
                  "Jane")  # Tuple -- immutable
# print(students_tuple[2])

print(students_tuple.count("Jane"))
print(students_tuple.index("Laxmi"))

team = tuple(["A", "B", "C", "D"])

print(type(team))

newlist = list(team)

print(type(newlist))
