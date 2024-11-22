#Python Program to Counts the Number of Times a Letter Appears in the Text File
def character_occurrence(file1,var):
          
          try:
               with open(file1,"r") as f1:
                        contents = f1.read()
                        contents = contents.lower()
                        var = var.lower()
                        print('number of spaces :{0}'.format(contents.count(var)))
          except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Counts the Number of Times a Letter Appears in the Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          var = str(input('Enter   the letter : '))
          character_occurrence(directory,var)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
