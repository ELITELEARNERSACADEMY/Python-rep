#Python Program to Find the Cumulative Sum of a List
# if first value occurs more than once, once encountered, we count the occurrence and remove it from the list 
def Remove(j, list1):
               new_list = [] 
               for i in list1:
                    if j != i:
                            new_list.append(i)
               return new_list


def cumulative_sum(list1):
               s = 0
               for i in list1:
                     s += list1.count(i) 
                     list1 = Remove(i, list1)
               return s


print('Python Program to Find the Cumulative Sum of a List')     
list_Var  = ['Hamza','Yousouf','Job','Mathew','Peter','No','Joshua','Carlos','Yes','Job','Peter']
print('List : ',list_Var)

print('cumulative sum: {0}'.format(cumulative_sum(list_Var)))

