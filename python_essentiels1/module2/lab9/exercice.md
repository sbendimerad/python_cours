# Estimated Time:
15 minutes

# Level of Difficulty:
Intermediate

# Task:
* Copy/Complete this code to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large).
* The start time is given as a pair of hours (0..23) and minutes (0..59).
* Example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
* Don't worry about any imperfections - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.
```
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
# put your code here

```
# Hint:
* using the % and // operators may be the key to success.

# Test Data :
```
Sample input:12 17 59
Expected output: 13:16

Sample input:23 58 642
Expected output: 10:40

Sample input:0 1 2939
Expected output: 1:0
```

