blocks = int(input("Enter the number of blocks: "))

height = 0
inlayer = 1

while blocks >= inlayer:

    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid: ", height)
