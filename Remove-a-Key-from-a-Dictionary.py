#Python program Remove a Key from a Dictionary

def         Remove():                     
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
                         
                        n = input('Enter key to delete : ')
                        
                        del numbers[n]
                        print(numbers)


Remove()
