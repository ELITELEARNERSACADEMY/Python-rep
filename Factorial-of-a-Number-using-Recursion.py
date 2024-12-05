#Python Program to Find the Factorial of a Number using Recursion

def fact(x):
               if x==0:
                         return 1
               else:
                         return x*fact(x-1)
                        
print('Find Factorial')                        
try:
             n = int(input('Enter number  :'))
except:
             print('Error , please enter an integer value')
             n = int(input('Enter number:'))

print(fact(n))
