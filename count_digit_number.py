#Python Program to Count the Number of Digits in a Number
def count_digit_number(num):
               counter = 0
               while num!=0:
                        counter +=1 
                        num //= 10
               return counter 
                
print('Counting the Number of Digits in a Number: ')
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
print(' sum: {0}'.format( count_digit_number(num)))
