#Python Program to Find Average of a List

def Average(x):
           sum1 = 0
           for i in x:
                sum1+= i 
           return sum1/len(x)

print('Python Program to Find Average of a List')
list_Var  = [1,42,4,545,75,78,2,9,232,5653,86542,3,2]
print('My List: ',list_Var)
print('Average : {0}'.format(Average(list_Var)))

