# Write a program to find the sum of all elements in a list.
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Enter a list of numbers\n")
l=[]
try:
 while True:
    l.append(int(input()))
except:
  sum=0
  for i in l:
    sum=sum+i
  print("Sum of list is: " + str(sum))    
