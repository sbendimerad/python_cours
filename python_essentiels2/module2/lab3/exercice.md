
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
We've written it using the following assumptions:

it accepts Latin letters only (note: the Romans didn't use whitespaces or digits)
all letters of the message are in upper case (note: the Romans knew only capitals)
Let's trace the code:

line 02: ask the user to enter the open (unencrypted), one-line message;
line 03: prepare a string for an encrypted message (empty for now)
line 04: start the iteration through the message;
line 05: if the current character is not alphabetic...
line 06: ...ignore it;
line 07: convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
line 08: get the code of the letter and increment it by one;
line 09: if the resulting code has "left" the Latin alphabet (if it's greater than the Z code)...
line 10: ...change it to the A code;
line 11: append the received character to the end of the encrypted message;
line 13: print the cipher.


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

