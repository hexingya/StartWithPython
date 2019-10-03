
filename = input('Enter a filename: ')

with open(filename, 'w') as fd:
    data = '''
        Hey there!
        Are you okay?
        Find your reason.
    '''
    fd.write(data)
    # fd.writelines(data)
