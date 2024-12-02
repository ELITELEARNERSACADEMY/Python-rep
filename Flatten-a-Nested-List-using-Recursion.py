#Python Program to Flatten a Nested List using Recursion
def Flatten_list(i,flat_list,list1):
            if i == list1.index(list1[-1]):
                   return flat_list
            else:
                    if type(list1[i]) ==type('strings') or type(list1[i]) == type(1) or type(list1[i]) == type(1.2):
                            return Flatten_list(i+1,flat_list.append(list1[i]),list1)
                    else: 
                              def offload(j,flat_list2,list2):
                                        if j == len(list2):
                                              return  flat_list2
                                        else:
                                              flat_list2.append(list2[j])
                                              return offload(j+1,flat_list,list2)
                                
                              flat_listx = offload(0,flat_list,list1[i])
                              return Flatten_list(i+1 ,flat_listx, list1)
  
print('Python Program to Flatten a Nested List using Recursion')  
list_Var  = [['Hamza','Yousouf'],['Job','Mathew','Peter','Bwalya'],['No','Joshua','Carlos','Yes','Job'],['Peter'],'John']
print('List: ',list_Var)
print()
print()
print()
flat_list =[]
print('Flattened List: {0} '.format(Flatten_list(0,flat_list,list_Var))) 

