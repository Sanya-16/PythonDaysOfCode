# Write a program to shuffle the elements of a list randomly.
import random
print("Enter a list\n")
l=[]
try:
 while True:
    l.append(int(input()))       
except:
 random.shuffle(l)         
 print(str(l))