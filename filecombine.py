#Write a Python program to combine the content of two file
#and store it in a single list and display the list.

#lets understand the code first...

f1=open("abc.txt","w")
n=input("Enter the Text : ")
f1.write(n)
f2=open("xyz.txt","w")
n=input("Enter the Text : ")
f2.write(n)
f1.close()
f2.close()
list1=[]
f1=open("abc.txt","r")
s1=f1.read()
for i in s1:
    list1.append(i)
f2=open("xyz.txt","r")
s2=f2.read()
for i in s2:
    list1.append(i)
print("File Contents : ",list1)
f1.close()
f2.close()
