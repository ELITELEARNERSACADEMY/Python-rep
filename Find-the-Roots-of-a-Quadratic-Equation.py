#Python Program to Find the Roots of a Quadratic Equation

import math as  mt 
def  Roots_Qua_equation(a,b,c):
       if c == 0:
                 print('Operation possible')
                 return False 
                 
       x_1 = (b - mt.sqrt(pow(b,2) - 4*a*c))/(2*c) 
       x_2 = (-b - mt.sqrt(pow(b,2) - 4*a*c))/(2*c)
       if x_1 == x_2:
                return x_1
       return x_1,x_2
       
def  Roots_Qua_equation_ab(a,b):
       if a == 0:
                 print('Operation possible')
                 return False 
       x_1 = mt.sqrt(b/a) 
       x_2 = -1*(mt.sqrt(b/a))

       if x_1 == x_2:
                return x_1
       return x_1,x_2

def  Roots_Qua_equation_abx(a,b):
       if a == 0:
                 print('Operation possible')
                 return False 
       return (b/a)
                   
                   

choice  = 1
while choice !=0 and (choice < 4):
         print('1. Equation : ax*x - b ')
         print('2. Equation : ax*x - bx')
         print('3. Equation : ax*x +bx +c')
         print('0. kill the program')
         choice = int(input(' : '))
         
         if  choice == 0:
                    choice = 0    
         elif     choice ==1:
                    try:
                             a = int(input('Enter valuer of a :'))
                             b = int(input('Enter valuer of a :'))
                    except:
                             print('Error , please enter integer values for a and b')
                             a = int(input('Enter valuer of a :'))
                             b = int(input('Enter valuer of b :'))

                    print('root :{0}'.format(Roots_Qua_equation_ab(a,b)))

         elif choice ==2:
                    try:
                             a = int(input('Enter valuer of a :'))
                             b = int(input('Enter valuer of b :'))
                    except:
                             print('Error , please enter integer values for a and b')
                             a = int(input('Enter valuer of a :'))
                             b = int(input('Enter valuer of b :'))
                    print('root(s) :{0}'.format(Roots_Qua_equation_abx(a,b)))
         elif choice ==3 :
                 try:
                        a = int(input('Enter valuer of a :'))
                        b = int(input('Enter valuer of a :'))
                        c = int(input('Enter valuer of a :'))
                 except:
                        print('Error , please enter integer values for a and b')
                        a = int(input('Enter valuer of a :'))
                        b = int(input('Enter valuer of a :'))
                        c = int(input('Enter valuer of a :'))

                 print('root(s): {0}'.format(Roots_Qua_equation(a,b,c)))
         else:
                   choice = 1



