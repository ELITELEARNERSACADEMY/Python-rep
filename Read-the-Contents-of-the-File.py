#Python Program to Read the Contents of the File
def read_file(directory):

                 try:
                      with open(directory) as f:
                              print(f.read())
                 except TypeError:
                        print('There was a fault in opening the file, either does exist, wrong directory')

try:
           directory = str(input('Enter file name or Directory'))
           read_file(directory)
except TypeError:
            print('Incorrect file name or incorrect directory')
