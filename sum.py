#Write a Python program to sum all the items in a dictionary.

def sa(first):
    sum=0   #Initilaizing as 0
    for i in first:
        sum=sum+first[i]    #adding value to sum
    return sum

x=int(input("Enter the number of keys in dictionary : "))
first = {}      #creating dictionary
for i in range(1,x+1):
    n=int(input("Enter the key : "))
    first[n]=n*n

print("Dictionary : ",first)
print("Sum : ",sa(first))
