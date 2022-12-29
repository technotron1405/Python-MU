#Write a Python Script to create a dictionary where key will be
#numbers and values will be factorial of that numbers. Eg. {1:1,2:2,3:6}


n=int(input("Enter the number of keys : "))
fact = {}       #creating dictionary

#defining the function
def facto(a):
    f=1
    for i in range(1,a+1):
        f=f*i       #factorial function
    return f

for i in range(1,n+1):
    k=int(input("Enter the key : "))
    fact[k]=facto(k)    #passing value

print(fact)
