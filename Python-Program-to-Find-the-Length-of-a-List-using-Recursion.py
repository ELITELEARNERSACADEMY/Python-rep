#Python Program to Find the Length of a List using Recursion
def len_list(size,x):
       if size == x.index(x[-1])+1:
            return size
       else:
            return len_list(size+1,x)
            
   
print('Python Program to Find the Sum of Elements in a List using Recursion')
list_Var  = [1,42,4,545,75,-738,78,2,9,232,-18,5653,86542,3,2,-34]
print('My List: ',list_Var)

print(len_list(1,list_Var))

