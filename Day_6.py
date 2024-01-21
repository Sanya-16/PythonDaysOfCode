# Write a program to count the occurrences of a specific character in a string.
def str_occur(string,char):
    counter=string.count(char)
    print("Count is :"+str(counter))
    
string=input("Enter a string: ")
char= input("Enter a character: ")
str_occur(string,char)

