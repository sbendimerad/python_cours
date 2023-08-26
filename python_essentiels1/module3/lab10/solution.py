c0 = int(input("Enter Starting Number: "))

counter = 0 

while c0 != 1:
    counter += 1
    if (c0 % 2 == 0):
        c0 = c0/2
        print(c0)
    else:
        c0 = (3*c0)+1
        print(c0)

print("steps : ",counter)





