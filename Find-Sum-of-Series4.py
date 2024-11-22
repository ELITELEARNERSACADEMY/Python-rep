#Program to Read a Number n and Print the Series “1+2+…..+n= “

def sum(n,n_list,somme):
          if n==0:
              n_list.append((str(n) + ' =  ')) 
              return n_list,somme + 1
          else:
               n_list.append((str(n) + ' + ')) 
               somme += n
               return sum(n-1,n_list,somme)
               
               
print('Program to Read a Number n and Print the Series “1+2+…..+n= “')
try:
      n = int(input('Enter  the value of N: '))
except:
       print('Error, Please an Integer for the value  of N :')
       n = int(input('Enter  the value of N: '))

n_list = []
n_list,somme = sum(n,n_list,0)
for i in n_list:
        print(i,end='')
print('{0}'.format(somme),)
