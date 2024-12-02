#Python Program to Remove the ith Occurrence of the Given Word in a List

def Remove(j, list1):
               new_list = [] 
               for i in list1:
                    if j != i:
                            new_list.append(i)
               return new_list


print('Python Program to Remove the ith Occurrence of the Given Word in a List')
list_Var  = ['Hamza','Yousouf','Job','Mathew','No','Joshua','Carlos','Yes','Job','Peter']
print('List : ',list_Var)
try:
          var = str(input('Enter the word :'))
except:
           print('Input error!,  enter  word format input value')

print('New List: {0}'.format(Remove(var.capitalize(),list_Var)))
