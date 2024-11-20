#Python Program to Find All Pythagorean Triplets in the Range

def  pythagorean(n):
             pythagorean_triplets = []
             for i in range(1,n+1):
                       for j in range(1,n+1):
                               for k in  range(1,n+1):
                                        if pow(i,2) == (pow(j,2)+pow(k,2)):
                                                        pythagorean_triplets.append((i,j,k))
                                                        
                                                        
             return pythagorean_triplets
             
             
print('Find All Pythagorean Triplets in the Range')
try:
         n =int(input('Range : '))
except:
         print('Error enter an integer  value for the range ')
         n =int(input('p : '))

print(pythagorean(n))
