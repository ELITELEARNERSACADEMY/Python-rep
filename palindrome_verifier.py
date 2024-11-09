#Python Program to Check if a Number is a Palindrome

def  palindrome_verifier(num):
           var = num
           reversed_nums = []
           original_list = []
           while(num!=0):
                        reversed_nums.append(num%10) 
                        num //=10
           original_list = list(reversed(reversed_nums))
           for i in range(0,len(original_list)):
                 if(reversed_nums[i] != original_list[i]):
                         return False
           return True                     


print('Number Palindrome Verifier')
try: 
      num = int(input('Enter  an integer number :'))
except:
      print('Please enter valid information')
      print('Try to Enter an Integer  value')


if palindrome_verifier(num) :
          print('is {0} a Palidrome number : {1}'.format(num,True))
else: 
         print('is {0} a Palidrome number : {1}'.format(num,False))
