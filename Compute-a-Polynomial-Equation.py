#Python Program to Compute a Polynomial Equation
def compute_polynomial(n,a):
                    poly = []
                    somme = 0 # for sum 
                    for i in range(n+1):
                          try:
                                     print('Enter a coefficient value for {0} power'.format(i),end=' :')
                                     coef = float(input(':'))
                          except:
                                     print('Error, please try enter a numeric value')
                                     print('Enter a coefficient value for {0} power'.format(i),end=' :')
                                     coef = float(input(':'))
                                                
                          poly.append(coef)
                          
                    for i in range(n+1):
                                 somme += poly[i]*pow(a,i)
                    return somme
                    
try:
              n = int(input('Enter a positive highest power of the Polynomial'))
              a = float(input('Enter a value of x ----> f(x) Polynomial'))
except:
              print('Error, please enter an positive integer value for the highest power')
              n = int(input('Enter a positive highest power of the Polynomial'))
              a = float(input('Enter a value of x ----> f(x) Polynomial'))


print('f({0}) = {1}'.format(a,compute_polynomial(n,a)))
