text = input("Enter text: ")

# remove all spaces...
text = text.replace(' ','')


def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False  # It's not a palindrome
    return True  # It passed all checks, it's a palindrome

