#Python Program to Count the Number of Lines in Text File
def file_lines(file1):
          
          try:
               with open(file1,"r") as f1:
                        contents = f1.readline()
                        print(len(contents))
          except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Count the Number of Lines in Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          file_lines(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory')    
