#Python Program to Extract Numbers from Text File
def file_lines(file1):
          
          try:
               with open(file1,"r") as f1:
                        numbers = []
                        number = []
                        for i in range(0,1000000):
                                 numbers.append((str(i))) 
                        contents = f1.read()
                        for i in numbers:
                                  if  i in contents:
                                            number.append(i)
                        for i in number:
                                      print(i,end=' ')
                        
          except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Extract Numbers from Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          file_lines(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
