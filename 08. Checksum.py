# Written using this tutorial: https://www.youtube.com/watch?v=g-zjgBGELH0. Comments added by me for understanding
# Generating a checksum is perfectly legal and in some scenarios encouraged and therefore a disclaimer is not needed

# Import libraries
import os
import hashLib

# Creates a hash of the file using SHA-256
def calculateSHA256(filePath):
    sha256Hash = hashLib.sha256()
    with open(filePath, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break  # Ends the infinite loop once there is no more data to hash
            sha256Hash.update(data)
    file.close()
    return sha256Hash.hexdigest()

# Check file integrity
def checkIntegrity(directoryPath):
    # Ends the check if specified directory does not exist
    if not os.path.exists(directoryPath) or not os.path.isdir(directoryPath):
        print(f"Directory: {directoryPath} does not exist.")
        return

    # If the directory exists, calculate and return a hash for each file
    for root, dirs, files in os.walk(directoryPath):
        for fileName in files:
            filePath = os.path.join(root, fileName)
            calculatedHash = calculateSHA256(filePath)
            print(f"File: {filePath}\nSHA-256 Hash: {calculatedHash}")


directoryToCheck = input("Enter the directory to check: ")
checkIntegrity(directoryToCheck)

"""
    Things I've Learned:
    1. How to use the hashLib library to generate checksums using the SHA-256 hashing algorithm
    2. How to use the os library to navigate a directory system
"""
