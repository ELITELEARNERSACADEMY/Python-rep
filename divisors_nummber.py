#Python Program to Find All the Divisors of an Integer
def divisor(x,num):
           if x <= num:
                  if num%x ==0:
                           print(x,end='  ')
                  return divisor(x+1,num)
           else:
                   return 1

print('Find All the Divisors of an Integer: ')
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
print(f'Divisors of {num}',end=' : ')
divisor(1,num)   
