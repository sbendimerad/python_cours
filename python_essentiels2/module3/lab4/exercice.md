# Estimated time
30-60 minutes

# Level of difficulty
Easy/Medium

# Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

* Your class will be called Timer. 
* Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).
* Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
* The class itself should provide the following facilities:

  * objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
  * The class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

* all object's properties should be private;
* consider writing a separate function (not method!) to format the time string.
* Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Fill the following code :
```

class Timer:
    def __init__( ??? ):
        #
        # Write code here
        #

    def __str__(self):
        #
        # Write code here
        #

    def next_second(self):
        #
        # Write code here
        #

    def prev_second(self):
        #
        # Write code here
        #
```

