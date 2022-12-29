#A pangram is a sentence that contains all the letters of the English
#alphabet at least once, for example: The quick brown fox jumps over the lazy dog.
#Your task here is to write a function to check a sentence to see if it is a pangram or not.



def para(str):      #defining the function and passing the value in it
    str1=str.lower()    #string will be converted into lower case
    alp="qwertyuiopasdfghjklzxcvbnm"        #checking the alphabets
    for c in alp:       #checking condition
        if c not in str1:
            return False
        return True

n=input("Enter the sentence : ") #accepting the user input
y=para(n)   #passing sentence into the function

if(y==True):
    print("Sentence is pangram")
else:
    print("Sentence is not pangram")
