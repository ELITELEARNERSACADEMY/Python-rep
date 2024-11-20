# Python Program to Form an Integer that has Number of Digits at 10’s Place &amp; LSD at 1’s Place
import random as rd
# will break a given value into single digits   
def breaker(num):
         figures_numList = []
         while num!=0:
                  figures_numList.append(num%10)
                  num = num//10
         return   figures_numList
         
def Form_number():
             while(True):
                 a = rd.randint(10,100000000000)
                 figures_numList =[]
                 figures_numList = breaker(a)

                 if figures_numList[1]== len(figures_numList):
                         if figures_numList[0] == figures_numList[1]:
                                      return a


print('Generate a Random Integer that has Number of Digits at 10’s Place &amp; LSD at 1’s Place')
print(f'Value Found: {Form_number()}')
