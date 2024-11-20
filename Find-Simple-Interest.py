#Python Program to Find Simple Interest
"""Simple Interest=P×r×n
P = Principal
r = Interest rate
n = Term of loan, in years"""
def simple_interest(p,r,n):
         return p*r*n
         

print('Find Simple Interest')
try:
         p =float(input('p : '))
         r = float(input('r :'))
         n = float(input('n :'))
except:
         print('Error enter a numeric value ')
         p =float(input('p : '))
         r =float(input('r :'))
         n = float(input('n :'))

print(f' simple interest: {simple_interest(p,r,n)}')
