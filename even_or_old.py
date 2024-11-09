#Python Program to Check Whether a Given Number is Even or Odd using Recursion
def even_or_old(num):
        if num%2==0:
                  print(f'{num} is Even')
        else:
                  print(f'{num} is old ')
                  
print('Check Whether a Given Number is Even or Odd using Recursion')                  
try:
            num = int(input('Enter a number :'))
except:
             print('Wrong value format !,try enter integer value ')
             num = int(input('Enter a number :'))
             
even_or_old(num)
