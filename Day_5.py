# Write a program to find the maximum and minimum values in a list.
print("Enter a list of numbers\n")
l=[]
a=0
b=0
try:
 while True:
    l.append(int(input()))
except:
  a=max(l)
  b=min(l)
print("Max: "+ str(a)+"\nMin: "+str(b))  