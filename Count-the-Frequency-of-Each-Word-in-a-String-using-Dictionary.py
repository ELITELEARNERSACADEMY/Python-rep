#Python Program to Count the Frequency of Each Word in a String using Dictionary

def wordFrequency(word,fruits):
           temp = list(fruits.values())
           print(temp.count(word))
           
fruits = {
                          '1': 'Banana',
                          '2': 'Apple',
                          '3': 'Guava',
                          '4': 'Lemon',
                          '5': 'Lemon',
                          '6': 'Peach',
                          '7': 'Avocado',
                          '8': 'Apple',
                          '9': 'Orange',
                          '10': 'Kiwi',     
    }
   
print('Program to Count the Frequency of Each Word in a String using Dictionary') 
print(fruits.values())
word = (str(input('Enter the world ?'))).capitalize()

wordFrequency(word,fruits)


