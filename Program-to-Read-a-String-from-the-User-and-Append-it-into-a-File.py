def append_content(file1,file2):
                   with open(file1,"r") as f1:
                            with open(file2,"a") as f2: 
                                   contents =  f1.read()
                                   f2.write(contents)
                                                           
print('Program to Append the Content of One File to the End of Another File')
try: 
          directory1 = str(input('Enter   the name or directory of the file 1 : '))
          directory2 = str(input('Enter   the name or directory of the file 2 : '))
          append_content(directory1,directory2)
          
except TypeError:
            print('wrong  Data entered, try to enter  a valid file name or Directory ')    
