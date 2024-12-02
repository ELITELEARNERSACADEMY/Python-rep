# Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import  random 

def genRandomNumber():
         list1 = []
         for i in range(1,21):
                  list1.append(random.randint(1,20))             
         return list1
          
print('Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List')
print('List of Radom numbers:',genRandomNumber())


