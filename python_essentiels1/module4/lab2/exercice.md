# Estimated Time:
20 minutes

# Level of Difficulty:
Medium


# Task:
`* Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given month/year pair (while only February is sensitive to the year value, your function should be universal).  you can (and should) use the previously written and tested function
```
def isYearLeap(year):
#
# your code from LAB 4.1.3.6
#

def daysInMonth(year, month):
#
# put your new code here
#
```

# Test Code :
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
