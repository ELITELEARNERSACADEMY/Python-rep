#Python Program to Check Whether a given Year is a Leap Year
def leapYear(year):
       if year%4==0:
             if  year%100 != 0:
                      print(f'{year} is a leap year')
             else:
                      print(f'{year} is not a leap year')
       else:
                      print(f'{year} is not a leap year')
    
print('Check Whether a given Year is a Leap Year: ')
   
try:
        year = int(input('Enter  Year '))
except:
         print('Error !!, please enter a numeric value ')
         year = int(input('Enter  Year'))

leapYear(year)    
