#Python Program to Calculate Grade of a Student
def average(x):
            if len(x)!=0:
                   return sum(x)/len(x)
            else:
                    return 0


print('Calculate Average Grade of a Student: ')
grades = []
try:
           name = str(input('student name: '))
           print('Enter the marks:')
           for i in range(6):
                     print(f'course',end='')
                     grades.append(float(input(' : ')))
except:
           print('Wrong type of information Enter')
           print('Please enter name in words form')
           print('and enter numeric marks  form')
           
print(f'Name: {name}')
print(f'Average grade: {average(grades)}')
