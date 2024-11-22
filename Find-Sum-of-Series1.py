#Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N
def sum(n,somme):
          if n==1:
              return somme +1
          else:
               somme += float(1/n)
               return sum(n-1,somme)
             
print('Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N')
try:
      n = int(input('Enter  the value of N: '))
except:
       print('Error, Please an Integer for the value  of N :')
       n = int(input('Enter  the value of N: '))

print('sum = {0}'.format(sum(n,0)))
