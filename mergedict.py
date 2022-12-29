#Write a Python script to merge two Python dictionaries

x = int(input("Enter the number of keys in dictionary 1 : "))
first = {}      #creating first dictionary
for i in range(1,x+1):  #checking range values from 1 to user defined value + 1
    n = int(input("Enter the key  : "))
    first[n] = n*n

y=int(input("Enter the number of keys in dictionary 2 : "))
second={}       #creating second dictionary
for i in range(1,y+1):
    n=int(input("Enter the key : "))
    second[n]=n*n

#printing both dictionaries
print("Dictionary 1 : ",first)
print("Dictionary 2 : ",second)

for i in first:
    second[i]=first[i]      #merging the dictionaries
print("Merged Dictionary :",second)

