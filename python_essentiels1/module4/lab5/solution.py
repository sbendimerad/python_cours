def isPrime(n):
 for i in(2,n):
     if n % i == 0 :
        continue
     return True



for i in range(1, 60):
    if isPrime(i + 1):
        print(i + 1, end=" ")





