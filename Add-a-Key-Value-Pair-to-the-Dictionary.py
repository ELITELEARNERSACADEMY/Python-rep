#Python Program to Add a Key-Value Pair to the Dictionary
def         Add():                     
                        #my dictionary               
                        numbers={
                                         'one' : 1,
                                         'two' : 2, 
                                         'three' : 3, 
                                         'four' : 4, 
                                         'five' : 5,
                        }
                        print('Keys: {0} '.format(numbers.keys()))
                        print('Values: {0} '.format(numbers.values()))
                         
                        n = int(input('How many Key value pair are you entering'))
                        
                        for i in range(n) :
                              key = input('Key : ')
                              value = input('Value : ')
                              numbers.update({key : value})
                        print(numbers)

Add()

