#Python program Multiply All the Items in a Dictionary

def Product(dict_name):
                product = 1
                for i in dict_name.values():
                         product *= i
                return product
                


#my dictionary               
numbers={
                 'one' : 1,
                 'two' : 2, 
                 'three' : 3, 
                 'four' : 4, 
                 'five' : 5,
}

print('{0}'.format(numbers.values()))

print('Product: {0}'.format(Product(numbers)))

