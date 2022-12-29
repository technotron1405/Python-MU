#Write a python code to display the odd and evennumbers separately from
#a list. (All elements in the list should be taken from user).



def splitevenodd(a): #defining the functtion
    evenlist =[]    #list for even numbers
    oddlist =[]     #list for odd numbers

    for i in a:
        if(i%2==0):
            evenlist.append(i)
        else:
            oddlist.append(i)

    print("Even list : ",evenlist)
    print("Odd List : ",oddlist)

    

a=list()    #creating list
n=int(input("Enter the size of first list : "))
print("Enter the element of first list : ")
for i in range(n):  #range limit - size of list
    k = int(input(""))
    a.append(k)     #inserting values

splitevenodd(a)     #calling function

    
