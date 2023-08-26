# Estimated Time:
10 minutes

# Level of Difficulty:
Medium


# Task:
* A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
* For example, 8 isn't a prime number, as you can divide it by 2 and 4. On the other hand, 7 is a prime number, as we can't find any legal divisors for it.

* Your task is to write a function checking whether a number is prime or not.
* The function:
  * is called isPrime;
  * takes one argument (the value to check)
  * returns True if the argument is a prime number, and False otherwise.
* Hint : try to divide the argument by all subsequent values (starting from 2) and check the remainder - if it's zero, your number cannot be a prime; think carefully about when you should stop the process.

# Test Code :
```
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()


Output : 2 3 5 7 11 13 17 19 

```
