#Python program Map Two Lists into a Dictionary

def   Map(list_key,list_value):
                key ,value ='none','none'
                my_dict = {}
                #get the length of the longest list 
                if len(list_key)>len(list_value):
                     n = len(list_key)
                else:
                      n =len(list_value)
                      
                for i in range(n):
                     key ,value ='none','none' # defaut values for key and value to be none, it the key or value does not exist
                     if i< len(list_key):# ensure that the range is not above the size of the list 
                          key = list_key[i]
                     if i< len(list_value):
                          value = list_value[i]
                          
                     my_dict.update({key:value})         # update dictionary 
                
                print()
                print('Dictionary content')             
                for content in my_dict:
                                  print('{0} : {1} ,'.format(content,my_dict[content]),end='  ')
                print()

print('Program Map Two Lists into a Dictionary')                        
list_key = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
list_value = ['Apple','Banana','Cat','Donkey','Eagle','Flag','Ghost','Home','Island','Jungle','Kit','Laundry','Mouth','Nose','Orange','Pineapple','Quit']
print('Keys : {0}{1} Values : {2}'.format(list_key,'\n',list_value))

Map(list_key,list_value)
