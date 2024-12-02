#Python Program to Remove All Tuples in a List Outside the Given Range


def delete_tuples(lower_var , upper_var , list_1):
                in_range_tuple = []
                for  i in range(len(list_1)):
                        if i >= lower_var and  i <=  upper_var :
                                  in_range_tuple.append(list_1[i])
                delete_tuple = tuple(list_1)
                del delete_tuple
                
                return in_range_tuple
                

print('Remove All Tuples in a List Outside the Given Range')

list_4_tuples = [('hello','good', 'well'),(1,28,2,7,3,9,278),('school','hospital','Bank'),('Male','Female'),('Red','Green','Blue')]
print('List of Tuples :',list_4_tuples)
print('Length of List : ',len(list_4_tuples))
try: 
     lower = int(input('Enter the Lower value for the Range'))
     upper =int(input('Enter the Upper value for the Range'))
except:
     print('Invalid input')
     print('Please enter integer values')
     exit()
     
print('New List of tuples: {0}'.format(delete_tuples(lower-1 , upper-1 , list_4_tuples)))
