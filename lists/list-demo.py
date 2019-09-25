# list --- mutable/changable

from collections import deque
browsers = ["Firefox", "Opera", "Safari", "Chrome"]

# print(browsers)
# # length of list
# print(len(numbers))
# print(mixed)

# print(browsers[1:3])

# browsers[len(browsers) - 1] = "Firefox"

# browsers[2:] = ["new browser", "old browser"]

# browsers[:] = ["new browser", "old browser"]

# browsers[:] = []

# browsers[0:1] = ["Chrome"]

# browsers[0] = "Brave"

# print(browsers)


#
# methods
#

mixed = ["apple", "orange", 2343, 34.34, ["app", "something"]]

# add item at the end
# mixed.append("Papaya")
# mixed.append("Orange")


# mixed.insert(0, "Computer")
# mixed.insert(len(mixed), "ComputerS")
# mixed.insert(3, "Holi")

# lastitem = mixed.pop()
# print(lastitem)

# del mixed[1]

# del mixed[:]
# mixed.clear()
# print(mixed)

numbers = [34, 3, 45, 5.7, 45, 0]

# remvoes first occurance
# numbers.remove(45)

# print(numbers.index(45))
# print(numbers.index(45, 3))

# print(numbers.count(0))

# numbers.sort()
# # browsers.sort(reverse=False)
# browsers.sort(reverse=True)

# print(numbers)
# print(browsers)


# print(mixed)
# mixed.reverse()
# print(mixed)

list1 = ['a', 'd', 'b']

# list2 is not a copy of list1
# list2 = list1

# list1[0] = 'x'

# print(list1)
# print(list2)

# list2 = list1[:]
# list2 = list1.copy()
# list1[1] = 'D'

# print(list1)
# print(list2)


# games = ['cricket', 'football', 'hockey', 'badminton']

# games.extend(['cricket', 'kabaddi'])

# games.extend("apple")

# print(games)

# stack --- last in first out
# queue --- first in first out

queue = deque(['apple', 'orange', 'guava'])

queue.appendleft('new fruit')
queue.appendleft('new fruit0')

queue.popleft()
# queue.popleft()


# print(queue)

#
# for loop & range function
#

# for x in range(4, 10):
#     print(x, end=" ")

# for i in "String":
#     print(i)

# for item in [34, 3, 4, "lock"]:
#     print(item)

#
# list comprehension
#

# squares = [x*x for x in range(100)]
# squares = [x*x for x in [3, 4, 5, 6]]
# new_string = [sitem.upper() for sitem in "The Quick brown fox"]

# cubes = [n**3 for n in range(10, 201, 10)]

# odd = [e for e in range(1, 41) if e % 2 != 0]

multiples_of_seven = [item for item in range(7, 1000) if item % 7 == 0]

print(multiples_of_seven)
