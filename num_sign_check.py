#Python Program to Check Whether a Number is Positive or Negative
def check_sign(x):
           if x>=0:
                 print(f'{x} is positive')
           else:
                  print(f'{x} is negative')

var =  input('Enter a number : ')
try:
      check_sign(float(var))
except:
      print('Please enter valid information')
      print('Try to Enter a number value')
