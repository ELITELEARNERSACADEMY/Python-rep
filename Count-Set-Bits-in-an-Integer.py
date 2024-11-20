#Python Program to Count Set Bits in an Integer

#converting integers to binary 
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
                        
count = 0

for i in  range(0,len(binaries)):
        if binaries[i] == 1 :
                 count+=1

print(f'{count} Bit(s)')
