#Python Program to Find Second Largest Number in a List

def second_to_Max(x):
        y = max(x) # get the max 
        x[x.index(y)] = 0 #find the index of max, initialize the value with 0, so that second max becomes max 
        return max(x)
        
        
print('Python Program to Find Second Largest Number in a List')
list_Var  = [1,42,4,545,75,78,2,9,232,5653,86542,3,2]
print('My List: ',list_Var)
print('2nd Max Value : {0}'.format(second_to_Max(list_Var)))


