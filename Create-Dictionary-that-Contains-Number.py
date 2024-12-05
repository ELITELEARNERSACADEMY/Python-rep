#Python Program to Create Dictionary that Contains Number

def create_dict(n):
         my_dict = {}
         for i in range(n):
                       key = str(input('Enter the key : '))
                       value = float(input('Enter a numeric value for the key : '))
                       my_dict.update({key:value})
                       
         print()
         print('Dictionary content')             
         for content in my_dict:
             print('{0} : {1} ,'.format(content,my_dict[content]),end='  ')
  
print('Program to Create Dictionary that Contains Number')  
n =  int(input(' Hey enter an integer for the range  of your key-Value pair  for dictionary of numbers'))
create_dict(n)
