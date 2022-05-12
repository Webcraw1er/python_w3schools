"""
open() function takes two parameters; filename and mode 
"r"     read    ; default mode, opens a file to read. error if the file does not exist
"a"     append  ; opens a file for appending. CREATES the file if not exist.
"w"     Write   ; opens a file for writing. CREATES a file if not exist
"x"     Create  ; creates the specified file, returns the file if it exists.

in addition you can decide if your file will be handled as text or binary.
"t"     text    ; default value, text mode
"b"     binary  ; binary mode(e.g. images)

"""

#1. to open a file you only need to specify the name
#f= open("demofile.txt")
#      since the default mode is "r" and "t", the above statement is same as
try:     
    f= open("demofile.txt", "rt")
except:
    print("fIle does not exist")
else: 
    print("File opened")



"""
instead of tryexcept, you can use the below blocks of codes.
f= open("demofile.txt", "rt")
if not(f):
    print("file does not exist")
else:
    print("file opened")

"""