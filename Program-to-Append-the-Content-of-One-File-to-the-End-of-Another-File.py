#Python Program to Read a String from the User and Append it into a File
def add_content(file1,content):
                   with open(file1,"a") as f1:
                                  f1.write(content)
                                                                        
print('Program to Append the Content of One File to the End of Another File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          var = str(input('Enter   data: '))
          add_content(directory,var)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
