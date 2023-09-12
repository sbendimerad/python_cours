secret_number = 777

gamer_number = int(input("Enter an integer number: "))

while gamer_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    gamer_number = int(input("Enter an integer number: "))

print("Well done, muggle! You are free now.")
