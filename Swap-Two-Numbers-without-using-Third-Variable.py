# Python Program to Swap Two Numbers without using Third Variable
import sys 

def swap_2_digits(num):
              a=str(num%10) +str(num//10)
              return int(a)
    
try: 
         num = int(input('Enter integer less than 100 : '))
except:
        print('Error ,Please a valid integer value')
        num = int(input('Enter integer between 9 and 100 : '))
 
if num >=100:
           raise TypeError('you are out of range ')
print('swapped digits: {0}'.format(swap_2_digits(num))) 

