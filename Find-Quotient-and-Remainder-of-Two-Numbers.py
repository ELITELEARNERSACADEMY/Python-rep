# Python Program to Find Quotient and Remainder of Two Numbers
def quotient(a,b):
        return b/a,b%a


print('Find Quotient and Remainder of Two Numbers')
try:
         a =float(input('a : '))
         b =float(input('b :'))
except:
         print('Error enter a numeric value ')
         a =float(input('a : '))
         b =float(input('b :'))

x,y = quotient(a,b)
print(f'Quotient: {x} Remainder {y}')
