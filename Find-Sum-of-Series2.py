#Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
#factorial function 
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
 
 #sum of  1/n! function  
def sum():
              somme = 0
              term = 1
              n = 1
              while abs(term) > pow(10,-10):
                              somme += term
                              n+=1
                              term = 1/fact(n)
                              
              return somme
             
print(' Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N')
try:
           print('sum = {0}'.format(sum()))
except TypeError:
       print('Error, ')


