#Python Program to Find Sum of Digits of a Number
def  sum_digit_num(num):
           somme = 0 #sum
           while(num!=0):
                        somme += num%10 
                        num //=10
           return somme
  
print('Find Sum of Digits of a Number: ')
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
print(' sum: {0}'.format( sum_digit_num(num)))
