# Written using this tutorial: https://www.youtube.com/watch?v=BFOex_Tysr8. I added comments to test my understanding
# No disclaimer this time, using forensic tools to recover deleted files is legal. Just make sure not to violate GDPR

# Import libraries
import os
from winreg import *

# Convert security identifier to human readable format
def sidToUser(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                        "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
                      + "\\" + sid)
        (value, type) = QueryValueEx(key, "ProfileImagePath")
        user = value.split("\\")[-1]
        return user
    except:
        return sid

# Find recycling directory. Specifies directories found across different operating systems and will therefore work universally
def returnDirectory():
    directories = ["C:\\Recycler\\", "C:\\Recycled\\", "C:\\$Recycle.Bin\\"]
    for recyclingDirectory in directories:
        if os.path.isdir(recyclingDirectory):
            return recyclingDirectory
        return None

# Find recycled files, taking the recycling directory as a parameter
def findRecycled(recyclingDirectory):
        directories = os.listsir(recyclingDirectory)
        for sid in directories:
            files = os.listdir(recyclingDirectory + sid)
            user = sidToUser(sid)
            print("\nListing files for user: " + str(user))
            for file in files:
                print("Found file: " +str(file))

# Main function
def main():
    recyclingDirectory = returnDirectory()
    findRecycled(recyclingDirectory)
    
main()

"""
Things I have learned:
    1. How to use os and winreg
    2. try/except
    3. How to convert Windows Security Identifiers to a human readable format
"""
