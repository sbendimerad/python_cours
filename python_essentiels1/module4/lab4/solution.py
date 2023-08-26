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
    


