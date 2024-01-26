# Create a program that checks if a year is a leap year.
year=int(input("Enter a year: "))
if year%4==0 and year%100!=0:
    print("Its a leap year")
else:
    print("Its not a leap year")
