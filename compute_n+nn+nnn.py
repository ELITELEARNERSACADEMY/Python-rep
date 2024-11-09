#Python Program to Read a Number n and Compute n + nn + nnn
def compute(n):
      return n+n**2+n**3


print('Compute n + nn + nnn: ')
try:
        n = float(input('Enter value of n:'))
except:
         print('Error !!, please enter a numeric value ')
         n = float(input('Enter value of n'))


print(f'{n}+{n**2}+{n**3} : {compute(n)}')
