#Python Program to Swap the First and Last Element in a List 
def swap(list1):
        temp = list1[0]
        list1[0] = list1[-1]
        list1[-1] = temp
        return list1
        
        
print('Python Program to Swap the First and Last Element in a List ')
list_Var  = [1,42,4,545,75,-23,3,1,-738,78,2,9,232,-18,2,5653,86542,3,2,-34]
print('List :',list_Var)
print('Swapped 1st and last value of the  list: ',swap(list_Var))

