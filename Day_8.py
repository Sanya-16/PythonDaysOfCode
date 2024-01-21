# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
def case(str1):
    lower=0
    upper=0
    for i in str1:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    print("Number of lowercase letters is: "+str(lower))
    print("Number of uppercase letters is: "+str(upper))

str1=input("Enter a string: ")
case(str1)                
   