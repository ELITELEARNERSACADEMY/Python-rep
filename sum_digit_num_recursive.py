#Python Program to Find Sum of Digit of a Number using Recursion

def sum_digit_num(num,somme):
      if num==0:
           return somme
      else:
            return sum_digit_num(num//10,somme=somme+num%10)

print('Find Sum of Digits of a Number: ')
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
print(' sum: {0}'.format( sum_digit_num(num,0)))
