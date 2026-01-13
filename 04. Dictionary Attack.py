# Made using this guide: https://www.youtube.com/watch?v=OLHwDiZYF8E. Comments added by me for understanding
# Disclaimer: made for display purposes, cracking passwords without consent is illegal

# Import libraries
import hashlib

def crackHash(inputPassword):
    # Open password list if it exists, and return an error if it doesn't
    try:
        passFile = open("wordlist.txt", "r")
    except:
        print("Could not find file")
        
    # Loop through the file, encode and hash each password and then compare it to the inputted hash
    # If the hashed password is the input hash, then the password is returned
    for password in passFile:
        hashedPassword = password.encode("utf-8")
        digest = hashlib.md5(hashedPassword.strip()).hexdigest()  # Removes whitespace and then hashes with MD5
        if digest == inputPassword:
            print("Password found: " + password)
    
    passFile.close()
    
crackHash("2ac9cb7dc02b3c0083eb70898e549b63")  # Translates to Password1




"""
    Things I learned:
        1. How to use try/catch in Python
        2. How to use hashLib to make and compare hashes
        
"""
