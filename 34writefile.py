"""
"a"     : append, will append to the end of the file.
"w"     : write, will overwrite any existing content
                    it fucking overwrites the entire file!

.write(): a method that lets you write after you open something.
"""
from tkinter import Y


print("\nbefore append:")
f= open("demofile.txt", "w")
f.write("this  file is for testing purposes.\nGood luck!\n-Justin")
f.close()

f= open("demofile.txt", "r")
print(f.read())
f.close

print("\nappend:")
f= open("demofile.txt", "a")
f.write("\nNow the file has one more line!\nmake it two!")
f.close()

f=open("demofile.txt", "r")
print(f.read())
f.close()

print("\nwrite:")
f=open("demofile.txt", "w")
f.write("this is how you troll the shit out of it.\nby deleting everything.")
f.close()

f= open("demofile.txt", "r")
print(f.read())

#2. create a file
print("\n2,")
try:
    f= open("demofile.txt", "x")
except:
    print("the file already exists!")
else:
    print("file created!")

f= open("demofile2.txt", "a")
if f:
    print("file successfully created!")
f.close()
f=open("demofile2.txt", "w")
f.write("a new file!")
f.close()
f=open("demofile2.txt", "r")
print(f.read())
f.close()

import os
i=0
for i in range(6):

    #f= open("demofile[i].txt", "w")    # this does not work; ends up creating "demofile[i]" for 6 times.
    #f= open("demofile%d.txt" % i, "w")     # this DOES WORK!!!!!!!!!!!!!!!
    f= open("demofile{0}.txt".format(i), "w")

    f.write("new file!")
    f.close()
    i+=1
    print("ok")

ans= input("Would you like to delete the files? type Y or N: ")
if ans== "Y":
    i=0
    for i in range(6):
        os.remove("demofile{0}.txt".format(i))

"""
1.
    "a"     : append, will append to the end of the file.
    "w"     : write, will overwrite any existing content
                    it fucking overwrites the entire file!

    .write(): a method that lets you write after you open something.

2. "x"      : create, returns error if the file exist
    "a"     : append, will create a file if the specified named file doesn;t exust.
    "w"     : write,            "

3. when removing you must import os
    and then use 
        os.remove() 
    method to delete files.
"""





