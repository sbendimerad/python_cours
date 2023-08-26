def isYearLeap(year):

    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return True
           else:
               return False
       else:
            return True
    else:
       return False


def daysInMonth(year, month):
    if month in [9, 4, 6, 11]:
        return 30
    elif month in [1,3,5,7,8,10,12]:
        return 31

    if isYearLeap(year) and month == 2:
        return 29  
    else :
        return 28

def dayOfYear(year, month, day):
    
    daysInMonth_count = 0
    for i in range(1,month):
        daysInMonth_count += daysInMonth(year,i) 
    daysInMonth_count = daysInMonth_count + day
    return daysInMonth_count
        
