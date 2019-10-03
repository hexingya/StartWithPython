# file reading

fd = open('demo.txt', 'r')  # returns file descriptor

# data = fd.read()  # file content
# data = fd.readline()  # a line of content(file)
data = fd.readlines()  # list of lines
fd.close()

print(data)

# for l in data:
#     print(l)


# fd = open('Zen.txt', 'r')
# # print(fd.readlines())
# for l in fd.readlines():
#     print(l)
# fd.close()

# with

with open('Zen.txt', 'r') as fd:
    for l in fd.readlines():
        print(l)
