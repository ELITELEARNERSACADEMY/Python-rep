import sys 
#Python Program to Test Collatz Conjecture for a Given Number
def Collatz_Conjecture_testor(n):
             while n!=1 :
                  if n%2==0:
                       n = n//2
                  else:
                       n = 3*n +1
                   
             return True
             
    
print('Test Collatz Conjecture for a Given Number')

try:
        n = int(input('Enter an integer number : '))
except:
         print('Error, Enter an integer : ')
         n = int(input('Enter an integer : '))
if n <= 0:
          print('Error, negative or zero values not allowed ')
          sys.exit()
print('Is {0} a Collatz Conjecture :{1}'.format(n,Collatz_Conjecture_testor(n)))
