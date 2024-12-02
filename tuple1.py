#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

def  tuples(a,b):
          t1=[]
          t2=[]
          t3=[]
          for i in range(a,b):
                  t1.append(i)
                  t2.append(pow(i,2))
          t1= tuple(t1)
          t2 =tuple(t2)
          t3.append((t1,t2))
          
          for content in t3:
                   print(content,end='')
          
print('Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number')
try:
          a =  int(input('Enter the  starting point :'))
          b =  int(input('Enter the  starting point :'))
          tuples(a,b)
except TypeError:
          print('Error, please enter integer values')
