#Python Program to Print Sum of Negative Numbers, Positive Even &am;  Odd Numbers in a List
def sum_list(x):
     even_list=[]
     old_list=[]
     negatives =[] 
     for i in x :
         if i<0:
              negatives.append(i)
         if  i>=0:    
            if i%2 ==0 :   
               even_list.append(i) # adding + even numbers to the list x 
            else:
              old_list.append(i)    # adding + old numbers to the list x 
              
     return f'Sum negatives: {sum(negatives)} Sum  +even: {sum(even_list)}, Sum  +old : {sum(old_list)}'

print('Python Program to Find Average of a List')
list_Var  = [1,42,4,545,75,-738,78,2,9,232,-18,5653,86542,3,2,-34]
print('My List: ',list_Var)
print(sum_list(list_Var))

