## Module 2 : Premier programme (La fct print)

#1
print("premiere phrase")
print()
print("seconde phrase")

print("premiere phrase\nseconde phrase")

print("\")                                                                                                            
print("\\")

#2
print("The itsy bitsy spider" , "climbed up")
print("My name is", "Python.")
print("Monty Python.")
print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


## Module 2 : Les types (String)

#1
print("I like \"Monty Python\"")
print('I like "Monty Python"')
print("\"i\'m\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

#2
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)

print(14 % 4)

#3
print(2 + 3 * 5)
print(9 % 6 % 2)
print(2 ** 2 ** 3)
print(2 * 3 % 5)
print((5 * ((2 % 3) + 10) / (2 * 5)) // 2)

## Module 2 : Les variables

1#
var = 1
print(var)

account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

var_s = "3.7.1"
print("Python version: " + var_s)

var = var + 1
print(var)

## Module 2 : Les commentaires

1#
"""
variable = variable op expression
variable op= expression
"""       
  
i = i + 2 * j ⇒⇒ i += 2 * j
var = var / 2 ⇒⇒ var /= 2
rem = rem % 10 ⇒⇒ rem %= 10
j = j - (i + var + rem) ⇒⇒ j -= (i + var + rem)
x = x ** 2 ⇒ x **= 2

2#
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)
x = x * 2
x *= 2

## Module 2 : La fonction input()

1#
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

anything = input("Enter a number: ")
something = anything ** 2
print(anything, "to the power of 2 is", something)

2#
anything = float(input("Enter a number: "))
something = anything ** 2
print(anything, "to the power of 2 is", something)

2#
print("ab"+"ba")
print("James" * 3)
print(3 * "an")
print(5 * "2")
        
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))

hyp = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is " + str(hyp))
