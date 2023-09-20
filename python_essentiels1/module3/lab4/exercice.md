# Estimated Time:
10 minutes

# Level of Difficulty:
Easy


# Task:


Due to astronomical reasons, years may be leap (366 days) or common (365 days). Since the introduction of the Gregorian calendar (in 1582), the following rules is used to determine the kind of year:

*on every year that is evenly divisible by 4
**  except every year that is evenly divisible by 100
***    unless the year is also evenly divisible by 400

* The code reads a year number, and needs to be completed to output one of the 3 messages : <br>
**Leap year  | Common year  | Not within the Gregorian calendar**
* Hint : use the != and % operators.

```
year = int(input("Enter a year: "))
# Put your code here.
```

# Test Data :
```
Sample input: 2000
Expected output: Leap year

Sample input: 2015
Expected output: Common year

Sample input: 1999
Expected output: Common year

Sample input: 1996
Expected output: Leap year

Sample input: 1580
Expected output: Not within the Gregorian calendar period
```
