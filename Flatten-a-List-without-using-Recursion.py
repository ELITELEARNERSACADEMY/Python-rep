#Python Program to Flatten a List without using Recursion
def Flatten_list(list1):
            flat_list = []
            for i in range(len(list1)):
                    if type(list1[i]) ==type('strings') or type(list1[i]) == type(1) or type(list1[i]) == type(1.2):
                        flat_list.append(list1[i])
                    else:
                         for j in list1[i]:
                              flat_list.append(j)
            return flat_list
  
print('Python Program to Flatten a List without using Recursion')  
list_Var  = [['Hamza','Yousouf'],['Job','Mathew','Peter','Bwalya'],['No','Joshua','Carlos','Yes','Job'],['Peter'],'John']
print('List: ',list_Var)

print('Flattened List: {0} '.format(Flatten_list(list_Var))) 

