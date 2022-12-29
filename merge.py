#Write a Python Code to merge the contents of two files into one file.

f1=open("abc.txt","w")
n=input("Enter the Text : ")
f1.write(n)
f2=open("xyz.txt","w")
n=input("Enter the Text : ")
f2.write(n)
f1.close()
f2.close()
f3=open("mno.txt","w")
f1=open("abc.txt","r")
s1=f1.read()
for i in s1:
    f3.write(i)
f1.close()
f2=open("xyz.txt","r")
s2=f2.read()
for i in s2:
    f3.write(i)
f2.close()
f3.close()
