#Find the Total Sum of a Nested List Using Recursion
"""
#using a loops 
def sum_Nested_list(list1):
            new_list = []
            for i in range(len(list1)):
                    if type(list1[i]) == type(1) or type(list1[i]) == type(1.2):
                        new_list.append(list1[i])
                    elif type(list1[i]) == type('String'):
                             print('The list is contains value you can\'t add: {0}'.format(list1[i]))
                             exit()
                    else:
                         for j in list1[i]:
                              new_list.append(j)
            return sum(new_list)

"""
def  sum_Nested_list(i,s,list1):
             if i == list1.index(list1[-1])+1:
                     return s
             else:
                      if type(list1[i]) ==type(1) or type(list1[i]) ==type(1.1):
                                   return sum_Nested_list(i+1,s+list1[i],list1)
                      else:
                                    return sum_Nested_list(i+1,s+sum(list1[i]),list1)
                                                       
print('Find the Total Sum of a Nested List Using Recursion')
list_Var  = [[1,42,4,545,75,-23],3,[1,-738],78,2,9,[232,-18,2,5653,86542,3,2],-34]
print('List :',list_Var)

print('Sum: {0}'.format(sum_Nested_list(0,0,list_Var)))

