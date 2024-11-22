# Python Program to Count the Number of Words in a Text File

def file_lines(file1):
           count_word = 0 
           try:
               with open(file1,"r") as f1:
                        contents = f1.read()
                        for  content in contents:
                                    if content == ' ':
                                            count_word += 1
                        print(count_word)
                        
           except TypeError:
                         print('There was  a problem when opening the file')
                         
print('Program to Count the Number of Words in a Text File')
try: 
          directory = str(input('Enter   the name or directory of the file : '))
          file_lines(directory)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
