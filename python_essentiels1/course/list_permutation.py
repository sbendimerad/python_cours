L= [0,1,2,3,4,5,6,7,8,9]
y=len(L)
z=-1
n=0
print(L)
for loop in range(y//2):
    L[n],L[z]=L[z],L[n]
    n+=1
    z-=1
    y-=1
    print(L)
