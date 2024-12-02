#Python Program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
def sort(list1):
          for i in range(len(list1)):
                 for j  in range(0,len(list1)-1-i):
                            if list1[j][-1] > list1[j+1][-1]:
                                        temp = list1[j]
                                        list1[j] =list1[j+1]
                                        list1[j+1] = temp
          return list1


print('Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple')

list_4_tuples = [('Hello','Good', 'Well'),('School','Hospital','Bank'),('Male','Female'),('Red','Green','Blue')]
print('List of Tuples :',list_4_tuples)
print('Length of List : ',len(list_4_tuples))
     
print('Sorted List of tuples: {0}'.format(sort(list_4_tuples)))
