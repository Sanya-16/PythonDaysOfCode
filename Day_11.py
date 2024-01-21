# Write a program to print the multiplication table of a given number.
def mult_table(num):
    # mul=1
    for i in range(1, 11):
      print(num, 'x', i, '=', num*i)
a=int(input("Enter a number: "))
mult_table(a)        