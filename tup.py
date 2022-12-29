def prime(n):
    p=1
    for i in range(2,n):
        if n%i==0:
            p=0
            break
        if p==1:
            return(n)
        else:
            return 0
        
tup=(10,5,12,11,33,100,17,7,13)
print(tup)
print("Prime Numbers : ")
for i in tup:
    n=prime(i)
    if n!=0:
        print(n)
