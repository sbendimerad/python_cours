# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord=input("enter a word : ")
userWord=userWord.upper()

wordWithoutVovels = ""

for letter in userWord:
    if letter in ["A","E","I","O","U"]:
        continue
    wordWithoutVovels += letter
    
    
print(wordWithoutVovels)
