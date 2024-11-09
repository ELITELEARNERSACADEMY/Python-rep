#Python Program to Convert Centimeters to Feet and Inches

def convert_cent(cent):
           print(f'Feet :{cent/30.48}')
           print(f'Inc\'s :{cent/2.54}')
 
 
print('Convert Centimeters to Feet and Inches: ')
try:
        num = float(input('Enter value '))
except:
         print('Error !!, please enter a numeric value ')
         num = float(input('Enter value'))


convert_cent(num)
