# Estimated time
20-25 minutes

# Level of difficulty 
Medium

# Scenario 
Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

* it should accept exactly one argument - a string;
* it should return a list of words created from the string, divided in the places where the string contains whitespaces;
* if the string is empty, the function should return an empty list;
* its name should be mysplit()
Use the following template
```
def mysplit(strng):
    # return [] if string is empty or contains whitespaces only
    
    # prepare a list to return

    # prepare a word to build subsequent words

    # check if we are currently inside a word (i.e., if the string starts with a word)

    # iterate through all the characters in string

        # if we are currently inside a string...

            # ... and current character is not a space...

                # ... update current word

                # ... otherwise, we reached the end of the word so we need to append it to the list...

                # ... and signal a fact that we are outside the word now

            # if we are outside the word and we reached a non-white character...

                # ... it means that a new word has begun so we need to remember it and...

                # ... store the first letter of the new word

    # if we left the string and there is a non-empty string in word, we need to update the list

    # return the list to invoker
```




