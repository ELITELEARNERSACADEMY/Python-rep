#Python Program to Reverse a Number
import math as mt
def reverse_number(num):
              reversed_nums =[]
              somme=0 #sum
              
              while(num!=0):
                        reversed_nums.append(num%10) 
                        num //=10
              print(reversed_nums)
              i = len(list(reversed_nums))
              print(i)
              j = 0
              while i >=0 and j < len(reversed_nums) :
                          somme += reversed_nums[j]*pow(10,i-1)
                          i-=1
                          j+=1
              
              return somme


print(reverse_number(482))
