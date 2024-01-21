# Write a function to count the number of vowels in a given string 
word=input("Enter a sentence:\n")
count=0
for x in word:
    if x in ("aeiouAEIOU"):
        count+=1
print("Number of vowels are: "+ str(count))