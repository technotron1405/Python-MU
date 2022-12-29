#Write a python code to display the sum of cubes of digits of a number using function.

def sumcube(n):     #defining the function
    sum = 0         #constant
    while(n>0):     #checking the condition
        x=n%10      #will result the remainder
        sum = sum + (pow(x,3))      #3 is  the power is the  cube
        n=n//10     #will resu;t  the qoutient

    print("Sum of cubes : ", sum)

n=int(input("Enter the number : "))
sumcube(n)

