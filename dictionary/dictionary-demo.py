# dictionary -- it's collection data type -- mutable -- indexing using key

counting = {1: "one", 2: "two", 3: "three"}

alphabets = {"A": "Apple", "B": "Ball", "C": "Cat"}

# print(counting)
# print(alphabets)
# print(type(counting))
# print(type(alphabets))

# print(len(alphabets))

# to get value using key index
# print(alphabets["B"])
# print(counting[2])

# to set vlaue using key index
# alphabets["A"] = "Animal"

# print(alphabets)

capitals = {"India": "New Delhi", "Nepal": "Kathmandu",
            "America": "Washington", "France": "Paris"}

# to copy or create new dictionary from existing one
# country_capital = capitals.copy()

# # to clear/empty a set
# country_capital.clear()

# print(country_capital)
# print(cpaitals)

# pop out and delete a specific item
# print(capitals.pop("Nepal"))
# print(capitals)

# popitem removes last inserted item
# print(capitals.popitem())
# print(capitals)

animals = {"Goat": "Grass", "Cow": "Grass",
           "Tiger": "Meat", "Human": "Plants and Meat"}

# to get all the keys
# print(animals.keys())

# to get all the values
# print(animals.values())

# to get all the keys and values
# print(animals.items())

# to get value of the specific key
# print(animals.get("Tiger"))
# print(animals['Tiger'])

# animals["Goat"] = "Green Plants"

# to change the value of existing key
# animals.update({"Goat": "Plants"})

# to change/add the vlaue/key-vlaue
# animals.update({"Ox": "Dry Grass", "Cow": "Green Plants"})

# print(animals)

sports = {"Cricket": 11, "Kabaddi": 7, "Badminton": 1, "Football": 11}

# if key exist then return the value
# print(sports.setdefault("Cricket"))

# if key does not exist then set the value with default vlaue (None)
# print(sports.setdefault("Wrestling"))
# print(sports.setdefault("Wrestling", None))
# print(sports.setdefault("Wrestling", ""))
# print(sports.setdefault("Wrestling", "***"))

# print(sports.fromkeys(("A", "B", "C", "E", "F")))
# print(sports.fromkeys(("A", "B", "C", "E", "F"), ""))
# print(sports.fromkeys(("A", "B", "C", "E", "F"), "something"))
print(sports.fromkeys(("A", "B"), "something"))

# Tuple as a key is allowed
# sports.update({("A", "B", "C"): "Alphabets"})

# List as a key is NOT allowed
# Error
# sports.update({["A", "B", "C"]: "Alphabets"})

print(sports)
