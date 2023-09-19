def mysplit(input_string):
    # Initialize an empty list to store the words
    words = []
    # Initialize an empty word to build each word
    current_word = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is not a space
        if char != ' ':
            # Add the character to the current word
            current_word += char
        else:
            words.append(current_word)
            current_word = ""  # Reset the current word
    
    # If there's a non-empty current word left, add it to the list of words
    if current_word:
        words.append(current_word)
    
    return words

# Example usage:
input_string = "To be or not to be, that is the question"
result = mysplit(input_string)
print(result)
# Output: ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
