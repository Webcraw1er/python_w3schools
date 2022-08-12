import os

print('<only print files under D:\TestFolder>')

def print_files_in_dir(root_dir, prefix):       # prefix here doesn't do anything. it only exists for the later
    files = os.listdir(root_dir)                # function: just to make indentations for the recursion.
    for file in files:
        path = os.path.join(root_dir, file)
        print(prefix + path)


if __name__ == "__main__":
    root_dir = 'D:\TestFolder'        #CAN ALSO WRITE AS      root_dir = os.getcwd()
    print_files_in_dir(root_dir, "")

print('\n\n <print all folders and files under D:\TestFolder>')
def print_files(root_dir, prefix):
    files= os.listdir(root_dir)
    for file_names in files:
        file_path=os.path.join(root_dir, file_names)        # you see here, the file_names are just names.
        print(prefix, file_path)                            # literally like file1, file2, file3... etc.
        if os.path.isdir(file_path):                        # in order to use this as a root_dir in recursions,
            print_files(file_path, prefix+ "\t  ")          # you have to join() them and make them full address.

if __name__ == "__main__":
    root_dir = 'D:/TestFolder/'        #CAN ALSO WRITE AS      root_dir = os.getcwd()
    print_files(root_dir, "")

print('<print TestFolder in the same directory>')       # if the target is in the same directory, the
if __name__ == "__main__":                              # prefix is "  ./  ".
    root_dir = "./TestFolder/"                          #   ex) ./TestFolder/
    for (root, dirs, files) in os.walk(root_dir):

        if len(dirs) > 0:
            for dir_name in dirs:
                print(" dir: " + dir_name)

            if len(files) > 0:
                for file_name in files:
                    print(" file: " + file_name)

#########  os.walk lets you do the same thing as above.  ##############3
# lets you search the minor folders with the for in.
# in for in ->
#       root: a path that contains dirs and files
#       dirs: directories under the root
#       files: files under the root
"""
1 the location of the current folder: 
    D:\Python\w3schools(PY)'

2. so what the hell is      __name__ == "__main__"      ?
    1) when a module is executed directly via the interpreter
            ex) python3 executeThisMoudle.py
        the __name__ variable comes with the value "__main__"

    2) however when a module is executed after the IMPORT, it has its own name on it instead of __main__
            ex) import executeThisMoudle.py
                executeThisMoudle.func()
    
"""