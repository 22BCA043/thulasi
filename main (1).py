# Leap Year

def isLeapYear(year):
 if(year % 4 ==0 and year % 100 !=0) or year % 400 == 0:
   return True 
 else:
   return False

year = int(input("enter a value:"))

if isLeapYear(year):
  print('{} is leap year.'.format(year))
else:
  print('{}is not a leap year.'.format (year))