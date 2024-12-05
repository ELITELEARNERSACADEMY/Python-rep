#Python program Create a Dictionary with Key as First Character and Value as Words Starting with that Character


def create_dict(n):
         my_dict = {}
         for i in range(n):
                       value = str(input('Enter a word or sentence : '))
                       key = value[0]                       
                       my_dict.update({key:value})
                       
         print()
         print('Dictionary content')             
         for content in my_dict:
             print('{0} : {1} ,'.format(content,my_dict[content]),end='  ')
  
print('Program Create a Dictionary with Key as First Character and Value as Words Starting with that Character')  
n =  int(input(' Hey enter an integer for the range  of your key-Value pair  for dictionary of numbers'))
create_dict(n)
