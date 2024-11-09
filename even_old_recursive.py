#Python Program to Check Whether a Given Number is Even or Odd using Recursion

#even_old checks weather the value x passed is even or old
def even_old(x):
            if (x%2==0):
                   print(f'{x} is an even number')
            else:
                   print(f'{x} is an old number')
                   
 #recursive looping through a list               
def recursive_loop(i,numbers):
             if i >= len(numbers):
                 return 1
             else:
                  even_old(numbers[i])
                  return recursive_loop(i+1,numbers)

#list declaration                 
numbers =[0,1,2,3,4,5,6,7,8,9,10]                  
recursive_loop(0,numbers)

