# Python Program to Capitalize First Letter of Each Word in a File
def capitalize_content(file1):
          try:
              with open(file1,"r") as f1:
                        contents = f1.read() 
                        print(contents.title())
          except TypeError:
                         print('Error when try to work on the file ')
                         
print('Program to Count the Occurrences of a Word in a Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          capitalize_content(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
