#Python Program to Split Even and Odd Elements into Two Lists
def split_list(x):
     even_list=[]
     old_list=[]
     for i in x :
         if i%2 ==0:   
              even_list.append(i) # adding even numbers to the list x 
         else:
              old_list.append(i)    # adding old numbers to the list x 
              
     return even_list,old_list
print('Python Program to Split Even and Odd Elements into Two Lists')
list_Var  = [1,42,4,545,75,78,2,9,232,5653,86542,3,2]
print('My List: ',list_Var)
even ,old  = split_list(list_Var) # initialize the value even all the values of list_Var && initialize the value even all the values of #value_Var

print('Evens : {0}'.format(even))
print('Evens : {0}'.format(old))
