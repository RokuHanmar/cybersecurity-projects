# Written using this tutorial: https://www.youtube.com/watch?v=Za0RzyfEoSI. Comments added by me for understanding
# Encrypting and decrypting data is perfectly legal and doesn't need a disclaimer

# Import libraries
from cryptography.fernet import Fernet

# Generate a key
def generateKey():
    return Fernet.generate_key()

# Saves the key by writing it to an external file
def saveKey(key, keyFile):
    with open(keyFile, "wb") as file:  # wb is "write in binary" and prevents changes to the key.
        file.write(key)
        file.close()

# Loads the key
def loadKey(keyFile):
    with open(keyFile, "rb") as file:  # rb is "read binary" and prevents changes to the key
        key = file.read()  # I've deferred from the tutorial here as Python best practices involve closing a file once done with it.
        file.close()  # As the tutorial simply returns the output, I have saved it as a variable and closed the file before return
    return key
    
# Encrypts data with a generated key then saves it to a different file
def encryptFile(inputFile, outputFile, key):
    with open(inputFile, "rb") as inputFile:
        data = inputFile.read()
        inputFile.close()
    
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(data)
    
    with open(outputFile, "wb") as outputFile:
        outputFile.write(encryptedData)
        outputFile.close()
    
# Decrypts data with a generated key then saves it to a different file
def decryptFile(inputFile, outputFile, key):
    with open(inputFile, "rb") as inputFile:
        data = inputFile.read()
        inputFile.close()
    
    fernet = Fernet(key)
    decryptedData = fernet.decrypt(data)
    
    with open(outputFile, "wb") as outputFile:
        outputFile.write(decryptedData)
        outputFile.close()

# Main program
key = generateKey()
keyFile = "encryptionKey.key"
saveKey(key, keyFile)

inputFile = "plaintext.txt"
encryptedFile = "ciphertext.txt"
decryptedFile = "formerCiphertext.txt"

encryptFile(inputFile, encryptedFile, key)
print(f"File {inputFile} encrypted to '{encryptedFile}'")

decryptFile(encryptedFile, decryptedFile, key)
print(f"File {encryptedFile} decrypted to '{decryptedFile}'")
"""
    Things I've Learned:
    1. How to use Fernet in symmetric key encryption and decryption
    2. The "wb" mode for writing to files, and "rb" for reading
    3. How to format string literals with print(f...)
"""
