def isPrime(num):
    if (num==1):
        return False
    elif (num==2):
        return True
    else:
        for i in range(2,num):
            if  num % i == 0 :
                return False # not prime
        return True
    


for i in range(0, 20):
	if isPrime(i + 1):
	    print(i + 1, end=" ")
print()


