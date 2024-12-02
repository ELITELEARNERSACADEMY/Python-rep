# Python Program to Find the Number Occurring Odd Number of Times in a List

def Count_old_num(list1):
             count = 0 
             for i in list1:
                 if i%2!=0:
                      count +=1
             return count
             
print('Python Program to Find the Number Occurring Odd Number of Times in a List')
list_Var  = [1,42,4,545,75,-23,3,1,-738,78,2,9,232,-18,2,5653,86542,3,2,-34]
print('List :',list_Var)
print(Count_old_num(list_Var),'Old numbers found')

