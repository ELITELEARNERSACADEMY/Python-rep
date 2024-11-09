#Python Program to Check Whether a Given Number is Even or Odd using Recursion

#even_old checks weather the value x passed is even or old
def even_old(x):
            if (x%2==0):
                   print(f'{x} is an even number')
            else:
                   print(f'{x} is an old number')
                   
 #recursive looping through a list               
def recursive_loop(i,numbers):
             if i >= len(numbers):
                 return 1
             else:
                  even_old(numbers[i])
                  return recursive_loop(i+1,numbers)

#list declaration                 
numbers =[0,1,2,3,4,5,6,7,8,9,10]                  
recursive_loop(0,numbers)


#Python Program to Check Whether a Number is Positive or Negative
def check_sign(x):
           if x>=0:
                 print(f'{x} is positive')
           else:
                  print(f'{x} is negative')

#Python Program to Print All Odd Numbers in a Range
def  old_num(numbers):
            print('Old numbers',end=' :')
            for i in range(len(numbers)):
                   if( numbers[i]%2 != 0 ):
                            print(f'{numbers[i]}',end=' ')
                            
old_num(numbers)

#Python Program to Check if a Number is a Palindrome

def reverse_num(num,list_numbers):
     if(num/10==0):
        return   list_numbers.append(num%10)
     else:
         list_numbers.append(num%10)
         num /= 10
         
def  palindrome_verifier(num):
           reversed_nums = reverse_num(num,empty_list)
           
           for i in range(len(reversed_nums)):
                     if(num%10 == reversed_nums[i] ):
                          num /= 10
                      else:
                          print(f'{num} is  palindrome')
                          return False
                          
             print(f'{num} is  palindrome')
             return True
