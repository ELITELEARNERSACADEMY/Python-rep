#Python Program to Print Largest Even and Largest Odd Number in a List

def Max(x):
     even_list=[]
     old_list=[]
     for i in x :
         if i%2 ==0:   
              even_list.append(i) # adding even numbers to the list x 
         else:
              old_list.append(i)    # adding old numbers to the list x 
              
     return f'Max even: {max(even_list)}, Max  old : {max(old_list)}'
    
print('Python Program to Print Largest Even and Largest Odd Number in a List')
list_Var  = [1,42,4,545,75,78,2,9,232,5653,86542,3,2]
print('My List: ',list_Var)
print(Max(list_Var))

