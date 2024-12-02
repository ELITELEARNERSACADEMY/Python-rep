# Python Program to Merge Two Lists and Sort it

def merger(list1,list2):
            for i in list2:
                   list1.append(i)
            return list1
             
def sort(list1):
             for i in range(len(list1)):
                  for j in range(0,len(list1)-1-i):
                             if int(list1[j]) > int(list1[j+1]):
                                  temporal_variable = list1[j]
                                  list1[j] = list1[j+1]
                                  list1[j+1]  = temporal_variable
              
             return  list1
                                  
                                  
print('Python Program to Merge Two Lists and Sort it')
list_Var  = [1,42,4,545,75,-738,78,2,9,232,-18,5653,86542,3,2,-34]
list_Var1 = [10,16,17,24,-23,21,8,292,-6,-11]


print('Merge: ',merger(list_Var,list_Var1))
print()
merged_list = list(merger(list_Var,list_Var1))
print('Sorted',sort(merged_list))

                                  

