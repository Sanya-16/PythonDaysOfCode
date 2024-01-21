# Write a program to remove duplicates from a list.
def remove_dup(l):
    r=[]
    for i in l:
        if i not in r:
            r.append(i)
    print("Final list is "+str(r))    
print("Enter a list of numbers\n")
l=[]
try:
 while True:
    l.append(int(input()))       
except:         
 remove_dup(l)
