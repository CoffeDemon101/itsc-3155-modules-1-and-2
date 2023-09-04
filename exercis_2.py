#Write a script that takes in a 
#string from the user. Print the 
#string where all the lower case 
#letters are shifted to the front 
#and the spaces removed. Keep the 
#relative order of the lower case 
#letters and upper case letters.

i = input("Enter a string:")
upper = ""
lower = ""
for one in i:
    if one.isupper():
        upper += one
    elif one.islower():
        lower += one
        
result = lower + upper
print(result)
