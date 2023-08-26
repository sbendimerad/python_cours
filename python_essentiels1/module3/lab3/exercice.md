# Estimated Time:
15 minutes

# Level of Difficulty:
Medium


# Task:

* Tax calculator : if the citizen's income <= 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents.
* If the income > 85,528, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
* Your tax calculator should accept one floating-point value: the income. 
* Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
* If the calculated tax is less than zero, it only means no tax (the tax is zero). Take this into consideration !

```
income = float(input("Enter the annual income: "))
#
# Put your code here.
tax = round(tax, 0)
print("The tax is:", tax, "thalers") 

```

# Test Data:
```
Sample input: 100000
Expected output: The tax is: 19470.0 thalers

Sample input: -100
Expected output: The tax is: 0.0 thalers

Sample input: 1000
Expected output: The tax is: 0.0 thalers
```

