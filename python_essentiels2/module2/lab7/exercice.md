# Estimated time
45 minutes

# Level of difficulty
Medium

# Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.
Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# Example:
if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

* you should use the two-argument variants of the pos() functions inside your code;
* don't worry about case sensitivity.

# Test Data
```
Sample input:
donor
Nabucodonosor

Sample output:
Yes
```
```
Sample input:
donut
Nabucodonosor

Sample output:
No
```
