# Write a program to print the first n numbers of a Fibonacci sequence
n=int(input("Enter limit: "))
a=0
b=1
c=0
print("1")
for i in range(n):
    c=a+b
    print(int(c))
    a=b
    b=c


