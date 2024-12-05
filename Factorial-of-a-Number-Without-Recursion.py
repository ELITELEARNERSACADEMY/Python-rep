#Python Program to Find the Factorial of a Number Without Recursion


def fact(x):
              fac = 1 
              while x !=0:
                      fac *=x
                      x-=1
              return fac 
             

print('Find Factorial')                        
try:
             n = int(input('Enter number  :'))
except:
             print('Error , please enter an integer value')
             n = int(input('Enter number:'))

print(fact(n))
