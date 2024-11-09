#Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3
print('Printing All Integers that Aren’t Divisible by Either 2 or 3:')
try:
       n = int(input('Enter the range'))
except:
       print('Error !!!, please enter numeric value')

for i in range(n+1):
       if i%2!=0 and i%3 !=0:
               print(i,end=' ')

