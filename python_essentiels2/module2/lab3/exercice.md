
# Estimated time
60-90 minutes

# Level of difficulty
Hard

# Context : The Caesar Cipher: encrypting a message

This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. 
The idea is rather simple - every letter of the message is replaced by its nearest consequent (A becomes B, B becomes C, and so on). 
The only exception is Z, which becomes A.
```
# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
```
# Scenario

You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

* asks the user for one line of text to encrypt;
* asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
* prints out the encoded text


# Test data
```
Sample input:

abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123
```
```
Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs
```  

