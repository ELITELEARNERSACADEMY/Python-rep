#Python Program to Find the Gravitational Force between Two Objects
#F = G*(m1*m2)/(r^2)


def Gravitational_Force(m1,m2,r):
                return (((6.674*pow(10,-11))*m1*m2) / pow(r,2))
            
print('Find the Gravitational Force between Two Objects')            
try:
          m1 = float(input('Enter the mass of Object 1: '))
          m2 = float(input('Enter the mass of Object 2: '))
          r = float(input('Enter the distance between two Object: '))

except:
           print('error , Enter a numeric Value')
           m1 = float(input('Enter the mass of Object 1: '))
           m2 = float(input('Enter the mass of Object 2: '))
           r = float(input('Enter the distance between two Object: '))


print(f'Gravitational Force: {Gravitational_Force(m1,m2,r)}')

