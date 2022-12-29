#Write a program that takes two lists and returns
#True if they have at least one common member.

n =int(input("Enter the number of elements in the list : "))
list1=[]    #array
for i in range(n):
    z=int(input("Enter the elements of list 1 : "))
    list1.insert(i,z)   #insertiong values in array one after the  another
print(list1)

m=int(input("Enter the number of elements in the list : "))
list2 = []
for j in range(m):
    z=int(input("Enter the elements of list 2 : "))
    list2.insert(j,z)   #insertiong values in array one after the  another
print(list2)

for a in list1:     #checking values in list1
    for b in list2: #checking values in list2 
        if a==b:    #cross checking values
            print("True")
        
