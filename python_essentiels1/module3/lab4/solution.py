Year = int(input("Enter a year: "))

"""if year > 1582 :
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               print("leap year")
           else:
               print("common year")
       else:
           print("leap year")
    else:
       print("common year")
else :
    print("not within the Gregorian calendar period")"""




if (Year % 4) == 0:
   if (Year % 100) == 0:
       if (Year % 400) == 0:
           print("{0} is a leap year".format(Year))
       else:
           print("{0} is not a leap year".format(Year))
   else:
       print("{0} is a leap year".format(Year))
else:
   print("{0} is not a leap year".format(Year))
