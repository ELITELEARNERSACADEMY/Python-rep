#Check if a Key Exists in a Dictionary or Not
def check_key(key,dict_name):
                     return (key in dict_name.keys())
                     
#my dictionary               
numbers={
               'one' : 1,
               'two' : 2, 
               'three' : 3, 
               'four' : 4, 
               'five' : 5,
}
print('Keys: {0} '.format(numbers.keys()))
key = input('Search key : ')


if check_key(key,numbers):
    print('{0}  exist'.format(key))
else:
    print('{0}  does not exist'.format(key))


