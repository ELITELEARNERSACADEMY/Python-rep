#Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range
print('Finding Numbers which are Divisible by 7 and Multiple of 5 in a Given Range:')
try:
       n = int(input('Enter the range'))
except:
       print('Error !!!, please enter numeric value')

for i in range(n+1):
       if i%7==0 and i%5 ==0:
               print(i,end=' ')

