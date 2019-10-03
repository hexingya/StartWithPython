# append data to the file

fd = open('Zen.txt', 'a')

fd.write('Apple ' * 100)
fd.close()
