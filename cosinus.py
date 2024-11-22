#Python Program to Find the Sum of Cosine Series
#factorial function 
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

 
 #sin(x)  sum of  ((-1)^n) *x^(2n+1)/(2n+1)! function  
 
def cos(x):
          somme = 0
          n = 0
          term = (pow(-1,n)*(pow(x,2*n)/fact(2*n)))
          
          while abs(term) > pow(10,-10):  
               somme +=term
               n=n+1
               term=(pow(-1,n)*(pow(x,2*n)/fact(2*n)))
          return somme
             
print('cos(x)')
try:
      x = float(input('Enter  the value of x: '))
      print('cos({0}) = {1}'.format(x,cos(x)))
except:
       print('Error, Please a Decimal  for the value of x :')

