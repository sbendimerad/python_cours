# Estimated Time:
30 minutes

# Level of Difficulty:
Medium

# Take the time to read : 

* There's one more thing we want to show you to make everything complete - it's recursion.

* This term may describe many different concepts, but one of them is especially interesting - the one referring to computer programming.

* In this field, recursion is a technique where a function invokes itself.

* These two cases seem to be the best to illustrate the phenomenon - factorials and Fibonacci numbers. Especially the latter.

# The Fibonacci numbers : 
* The Fibonacci numbers definition is a clear example of recursion. We already told you that:
  * ```Fibi = Fibi-1 + Fibi-2```
  * The definition of the ith number refers to the i-1 number, and so on, till you reach the first two.
  * Can it be used in the code? Yes, it can. It can also make the code shorter and clearer.

The second version of our fib() function makes direct use of this definition:
```
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

```

The code is much clearer now.

But is it really safe? Does it entail any risk?

Yes, there is a little risk indeed. If you forget to consider the conditions which can stop the chain of recursive invocations, the program may enter an infinite loop. You have to be careful.

# The Factorial  : 

* The factorial has a second, recursive side too. Look:
  * n! = 1 × 2 × 3 × ... × n-1 × n
  * It's obvious that:
  * ```1 × 2 × 3 × ... × n-1 = (n-1)!```
  * So, finally, the result is:
  * ```n! = (n-1)! × n```

This is in fact a ready recipe for our new solution.
```
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

```

Does it work? Yes, it does. Try it for yourself.

Our short functional journey is almost over. The next section will take care of two curious Python data types: tuples and dictionaries.
