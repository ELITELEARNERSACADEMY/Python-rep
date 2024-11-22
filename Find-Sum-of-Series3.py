#Python Program to Find the Sum of the Series: 1 + (x^2)/2 + (x^3)/3 + … (x^n)/n
#power 
def exp(x,n):
         result = 1
         while n>0:
                 result *=x
                 n-=1
         return result
          
 #sum of  x^n/n function  
def sum(x):
          somme=0
          term =1
          n =1
          while term > pow(10,-10):
               somme += term 
               n+=1
               term = exp(x,n)/n
               if n> 1001:
                      print('Serie diverges : sum = infinity')
                      exit()
          return somme
             
print('Find Sum of Series Find the Sum of the Series: 1 + (x^2)/2 + (x^3)/3 + … (x^n)/n')
try:
           x = float(input('Enter the value of x :'))
           print('sum = {0}'.format(sum(x)))
except TypeError:
       print('Error, ')

