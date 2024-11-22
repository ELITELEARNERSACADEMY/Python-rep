#Python Program to Count the Occurrences of a Word in a Text File
def file_lines(file1):
          
          try:
               with open(file1,"r") as f1:
                        contents = f1.read()
                        print('number of spaces :{0}'.format(contents.count(' ')))
          except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Count the Occurrences of a Word in a Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          file_lines(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
