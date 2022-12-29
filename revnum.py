#Write a python script to create a dictionary where key will be numbers
#and value will be its reverse of that number.
#For Example: dic1={123:321,89:98,236:632}


n = int(input("Enter the number of keys : "))
reverse = {}    #creating dictionary
def revnum(num):
    rev = 0
    while(num>0):
        rem = num%10    #remainder
        rev = (rev*10) + rem    
        num = num//10   #quotient
    return rev

for i in range(1,n+1):
    k=int(input("Enter the key : "))
    reverse[k] = revnum(k)  
print(reverse)
