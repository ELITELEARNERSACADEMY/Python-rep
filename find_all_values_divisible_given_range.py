#Python Program to Print All Numbers in a Range Divisible by a Given Number
print('Finding All Numbers in a Range of 200 to 500 Divisible by a Given Number:')
try:
       n = int(input('Enter the range'))
except:
       print('Error !!!, please enter numeric value')

for i in range(200,500+1):
       if i%n == 0:
               print(i,end=' ') 
