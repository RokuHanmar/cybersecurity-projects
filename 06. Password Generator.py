# Written using this tutorial: https://www.youtube.com/watch?v=F2ayXqbnpuo7. Comments added by me for understanding
# Generating a password is completely legal and has no need for disclaimers

# Import libraries
import random
import string

# Generates a password by creating a list of all ASCII letters (upper and lowercase), numbers and special characters.
# It then joins them together at random x number of times (where x is length) and returns the result
def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

passwordLength = int(input("Enter a password length: "))
if passwordLength < 1:
    print("Error: password must have at least 1 character")
else:
    generatedPassword = generatePassword(passwordLength)
    print("Your password is: " + generatedPassword)

"""
    Things I've learned:
    1. How to use the string library
    
"""
