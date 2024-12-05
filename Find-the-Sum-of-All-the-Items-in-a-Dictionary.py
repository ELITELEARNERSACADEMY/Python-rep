#Python program Find the Sum of All the Items in a Dictionary

def Sum(dict_name):
                return sum(dict_name.values())
                


#my dictionary               
numbers={
                 'one' : 1,
                 'two' : 2, 
                 'three' : 3, 
                 'four' : 4, 
                 'five' : 5,
}

print('{0}'.format(numbers.values()))

print('Sum: {0}'.format(Sum(numbers)))

