#Python Program to Count Occurrences of Element in List
def count_occurence(value,x):
            count = 0
            value = str(value)
            for i in x:
                 i = str(i)
                 if i == value:
                      count += 1
            return count
"""
alternatively 
def count_occurence(value,x):
       return x.count(value)
"""

print('Python Program to Count Occurrences of Element in List')
list_Var  = [1,42,4,545,75,-738,'Cat',78,2,9,232,'Dogs',-18,2,5653,'john',4,-18,86542,3,2,-34,'john','Peter','Kelvin']
print('My List: ',list_Var)


value = input('Enter  a the Value ')       
print(count_occurence(value,list_Var))

