#Python Program to Find All the Divisors of an Integer
def divisor(x,num,y):
      while(num!=0):
           if x <= num:
                  if num%x ==0:
                           y.append(x)
                  return divisor(x+1,num,y)
           else:
                   return min(y)

print('Find All the Divisors of an Integer: ')
divisors = []
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
print(f'Smallest divisor of {num}',end=' : ')
print(divisor(1,num,divisors))   

