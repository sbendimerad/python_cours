# Estimated time
30-60 minutes

# Level of difficulty
Easy/Medium

# Scenario
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:
Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

* objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
* the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
* all object's properties should be private;

Complete the code template : 

```
class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    # Write code here.
    #

    def __init__(self, day):
        #
        # Write code here.
        #

    def __str__(self):
        #
        # Write code here.
        #

    def add_days(self, n):
        #
        # Write code here.
        #

    def subtract_days(self, n):
        #
        # Write code here.
        #
```
