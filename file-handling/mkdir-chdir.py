import os


def filecreator(nf=10, ftype=".txt"):
    try:
        for c in range(nf):
            os.mkdir("Dun" + str(c))
            os.chdir("Dun" + str(c))

            with open(f"File{str(c)}{ftype}", 'w') as fd:
                fd.write(f"File {str(c)}")

            os.chdir("..")
    except FileExistsError:
        print('Error: Directory with same name')
    except:
        print('Something went wrong')

# to remove directory


def filedestoryer(nf=10, ftype=".txt"):
    try:
        for i in range(nf):
            os.chdir("Dun"+str(i))

            filename = f"File{str(i)}{ftype}"
            with open(filename) as fd:
                os.remove(filename)

            os.chdir('..')
            os.rmdir('Dun'+str(i))
    except FileNotFoundError:
        print('File or directory not found')


# filecreator(4, '.docx')
filedestoryer(2, '.docx')
