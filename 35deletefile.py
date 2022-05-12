"""
1. to delete a file, you must import the os.

"""
import os
if os.path.exists("demofile0.txt"):
    os.remove("demofile0.txt")
else:
    print("does not exist")

if os.path.exists("demofile0.txt"):
    os.remove("demofile0.txt")
else:
    print("does not exist")

    
try:
    f= open("demofile0.txt", "x")
except:
    print("failed!")