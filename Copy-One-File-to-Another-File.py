#Python Program to Copy One File to Another File
def  copy_file(file1,file2):
      contents = []
      try:   
             with open(file1,"r") as f1:
                    with open (file2,"w") as f2:
                               contents = f1.read()            
                               for content in contents:
                                           f2.write(content)            
                                 
      except TypeError:
                      print('There was a problem in opening the file')

print('Program to Copy One File to Another File')
try: 
          directory1 = str(input('Enter   the name or directory of the file 1: '))
          directory2 = str(input('Enter   the name or directory of the file 2:  '))
          copy_file(directory1, directory2)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')
