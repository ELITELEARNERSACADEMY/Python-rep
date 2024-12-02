#Python Program to Find the Intersection of Two Lists
def intersection(list1,list2):
               intersection_list = []
               for i in list1:
                       if (i in list2):
                             intersection_list.append(i)
               return  intersection_list
   
   
print('Python Program to Find the Intersection of Two Lists')     
list_Var  = ['Hamza','Yousouf','Job','Mathew','Peter','Bwalya','No','Joshua','Carlos','Yes','Job','Peter']
list_Var1 = ['Hildah','Charity','Bwalya','Carlo','Judith','No']
print('1st List: ',list_Var)
print('2nd List: ',list_Var1)

print('Intersection List: {0} '.format(intersection(list_Var,list_Var1))) 

