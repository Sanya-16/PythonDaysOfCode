#Write a program to check if a number is positive, negative, or zero.
def check_num(num):
    if num==0:
        print("Number is zero")
    elif num>0:
        print("Number is positive")
    else:
        print("Number is negative")        

num=int(input("Enter a number: ")) 
check_num(num)        