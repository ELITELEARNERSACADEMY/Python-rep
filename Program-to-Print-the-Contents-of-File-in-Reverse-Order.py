# Python Program to Print the Contents of File in Reverse Order
def reserve_content(file1):
          try:
               with open(file1,"r") as f1:
                        contents = f1.read()                        
                        print(contents[::-1])
          except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Print the Contents of File in Reverse Order')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          reserve_content(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
