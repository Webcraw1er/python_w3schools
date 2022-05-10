"""
1. checking if there is a pip installed -> use the command prompt.

2. PIP is a package manager for python packages.
    a package contains all the files you need for a module.
    modules are python libraries you can include in your project.


"""
#1. camelcase capitalizes the first letters of the words.
import camelcase
c= camelcase.CamelCase()
txt= "hello world"
print(c.hump(txt))


"""
1. 패키지 다운하려면: navigate all the way to the "Scripts" folder, and then type the following:
        pip install packageName


2. 설치된 패키지 확인: 다시 Scripts 찾아가서 pip list 친다.
"""