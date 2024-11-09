#Python Program to Print Table of a Given Number
def table_number(n):
         i =0
         while n>=i:
               print(f'{i} x {n} : {n*i}')   
               i +=1

print('Print Table of a Given Number: ')
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))

table_number(num)
