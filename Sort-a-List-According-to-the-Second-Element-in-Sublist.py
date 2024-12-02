# Python Program to Sort a List According to the Second Element in Sublist

def sort(list1):
       for i in range(len(list1)):
                 for j in range(0,len(list1)-1-i):
                       if list1[j][1] > list1[j+1][1]:
                                  temp = list1[j][1] #temp is a temporary variable
                                  list1[j][1] = list1[j+1][1]
                                  list1[j+1][1] = temp
       return list1
       
       
print(' Python Program to Sort a List According to the Second Element in Sublist')
list_Var  = [[1,42,4,5],[45,75,-23,3],[-738,78,2,9,232,-18],[5653,86542],[-34,16,62]]
print('List :',list_Var)
print('sorted: ',sort(list_Var))

