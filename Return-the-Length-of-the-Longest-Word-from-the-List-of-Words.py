#Python Program to Return the Length of the Longest Word from the List of Words
def  longest(list1):
        check = list1[0]
        for i in list1:
               if len(check) < len(i):
                       check = i
        return check, len(check)
        
print('Python Program to Return the Length of the Longest Word from the List of Words')
list_Var  = ['Hamza','Yousouf','Mathew','Joshua','Carlos']
print('List :',list_Var)

name,length = longest(list_Var)
print('Name : {0} Length : {1}'.format(name,length))

