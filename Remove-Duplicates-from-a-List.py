#Python Program to Remove Duplicates from a List

def removeDuplicate(list1):
        none_duplicate_list = []
        for i in list1:
              if list1.count(i) == 1 :
                      none_duplicate_list.append(i)
        return none_duplicate_list    
                       



print('Python Program to Remove Duplicates from a List')
list_Var  = [1,42,4,545,75,-23,3,1,-738,78,2,9,232,-18,2,5653,86542,3,2,-34]
print('List :',list_Var)
print('None Duplicate list',removeDuplicate(list_Var))

