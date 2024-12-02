#Python Program to Find the Sum of Elements in a List using Recursion

def sum1(i,sum_value,x):
    if i == -len(x)-1:
        return sum_value
    else:
        return sum1(i-1,sum_value + x[i],x)
        
print('Python Program to Find the Sum of Elements in a List using Recursion')
list_Var  = [1,42,4,545,75,-738,78,2,9,232,-18,5653,86542,3,2,-34]
print('My List: ',list_Var)

print(sum1(-1,0,list_Var))

