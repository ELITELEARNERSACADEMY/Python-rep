#Python Program to Print Binary Equivalent of an Integer using Recursion

def  integer_to_binary(x,binaries):
                   if x ==0:
                          return binaries;
                   else:
                         binaries.append(x%2)
                         return integer_to_binary(x//2,binaries)

print('Binary Equivalent of an Integer: ')
binary = []
try:
        num = int(input('Enter an integer number '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number '))
         
if num !=0:
     binaries = list(integer_to_binary(num,binary))
     i = len(binaries)-1
     while i >=0:
              print(binaries[i],end='')
              i-=1
     
else:
        print(0)
                        
