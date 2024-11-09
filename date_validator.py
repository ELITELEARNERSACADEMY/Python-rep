#Python Program to Check if a Date is Valid and Print the Incremented Date if it is
#dd-mm-yyyy    dd/mm/yyyy

def date_validator(date):
     if len(date)==10:
             day = int(date[:2])
             month = int(date[3:5])
             year = int(date[-4:])
       
             if day <= 31 and day >0 :
                  if month <= 12 and month >0:
                        if year >= 1000 and year <=9999:
                              print(f'{day}-{month}-{year+1}')
                        else:
                               print('Invalid Year')
                  else:
                        print('Invalid month')
             else:
                        print('Invalid day')
     elif len(date)== 8:
             day = int(date[:1])
             month = int(date[2:3])
             year = int(date[-4:])
       
             if day <= 31 and day >0 :
                  if month <= 12 and month >0:
                        if year >= 1000 and year <=9999:
                              print(f'{day}-{month}-{year+1}')
                        else:
                               print('Invalid Year')
                  else:
                        print('Invalid month')
             else:
                        print('Invalid day')



print('Check if a Date is Valid and Print the Incremented Date if it is')     
try:
         date = str(input('Enter date: dd-mm-yyyy / d/m/yyyy :'))
except:
          print('Wrong Date format')
          print('dd-mm-yyyy / dd/mm/yyyy')
          date = str(input('Enter date: dd-mm-yyyy / d/m/yyyy :'))

date_validator(date)
