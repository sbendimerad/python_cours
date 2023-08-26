# Estimated Time:
20 minutes

# Level of Difficulty:
Medium


# Task:

* Another function we're about to write is factorials. Do you remember how a factorial is defined? 
* It's marked with an exclamation mark, and is equal to the product of all natural numbers from one up to its argument.
```
0! = 1 (yes! it's true)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n
```
* Start by the following code :
```
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

   # Write your code here
```
# Test Code :
```
for n in range(1, 6):  # testing
    print(n, factorial_function(n))
```
