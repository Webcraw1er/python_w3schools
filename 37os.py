"""

os 는 operating system 의 약자.
it lets you do excecutions you do in your terminal.
    such as using py to copy and paste a file or creating
    a dir/ picking up file names in dir.

one popular fuinction is 
    os.getcwd()
        it gives you the current address(folder) you are in,
    os.listdir()
        gives you the array of all the files and folders in the dir.
        thus lets you use the "for in"
            ex) for file_name in os.listdir('c:/anaconda3'):
                    if file_name.endswith('exe'):
                        print(file_name)
    os.path.join()
        lets you concatenate address or path
            ex) os.path.join("C:/User/", "31path.py")
    os.path.isdir(path)
        lets you determine if the given path is a directory or not.
"""