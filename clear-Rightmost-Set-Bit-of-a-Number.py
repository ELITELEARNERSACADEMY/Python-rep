#. Python Program to Clear the Rightmost Set Bit of a Number

def  integer_to_binary(x,binaries):
                   if x ==0:
                          return binaries;
                   else:
                         binaries.append(x%2)
                         return integer_to_binary(x//2,binaries)

print('Count Set Bits in an Integer: ')
binary = []
try:
        num = int(input('Enter an integer number:  '))
except:
         print('Error !!, please enter a numeric value ')
         num = int(input('Enter an integer number: '))
         
binaries = list(integer_to_binary(num,binary))
print(f'Before : ',end= ' ')
for  i in range(0,len(binaries)):
        print(binaries[i],end=' ')

print('')
print('After : ',end= ' ')
for  i in range(0,len(binaries)-1):
        print(binaries[i],end=' ')

print('')

