year = int(input("Enter a year: "))

if year >= 1582:
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
else:
    print("not within the Gregorian calendar period")
