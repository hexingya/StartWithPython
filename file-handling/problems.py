
# try:
#     fd = open('File1.txt')
#     print(fd.read())
# except FileNotFoundError:
#     print('No file')
# except:
#     print('Something went wrong')
# finally:
#     print('File operation completed')


# fd = open('File1.txt', 'r')
# print(fd.read())
# fd.close()

with open('File1.txt', 'r') as fd:
    print(fd.read())
