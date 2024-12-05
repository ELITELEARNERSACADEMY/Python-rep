def         concatenate():                     
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
                         
                        print('New Dictionary has been created ')
                        n = int(input('How many Key value pair are you entering'))
                        temp = {}
                        for i in range(n) :
                              key = input('Key : ')
                              value = input('Value : ')
                              temp.update({key : value})
                        numbers.update(temp)
                        print(numbers)
concatenate()
