#Python Program to Find the Area of a Triangle

def area_tri(width,height):
       return (0.5*width*height)


print('Find the Area of a Triangle')
try:
         width =float(input('Width : '))
         height =float(input('height :'))
except:
         print('Error enter a numeric value ')
         width =float(input('Width : '))
         height =float(input('height :'))

print(f'Area: {area_tri(width,height)}')
