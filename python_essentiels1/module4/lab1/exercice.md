# Estimated Time:
20 minutes

# Level of Difficulty:
Medium


# Task:
Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise (Start with the module 3/lab 4 code) 

```
def isYearLeap(year):
	#
	#Put your code here
	#
```

* Note: we've also prepared a short testing code, which you can use to test your function.
* The code uses two lists - one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.

# Test Code :

```
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]


for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
	print("OK")
    else:
	print("Failed")
```




