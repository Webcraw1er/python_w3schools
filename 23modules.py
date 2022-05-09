"""
1. module is lib in c
2. it is really, a code library.
3. elaborately, its a file that contains a set of functions you want to include in your application
4. creating a module: just save the code you want in a file with a file extension .py
    ex)
        save the following code as mymodule.py.
            def greeting(name):
                print("Hello, ", +name)

    Then we use the import statement to use the model.
    ex)
        import mymodule
            mymodule.greeting("Johnathan")
    
    SO THE SYNTAX IS 
        moduleName.functionName(parameter)

"""
#1. calling from a module.
print("\n1.")
from re import X
import module23

module23.myfunc1("Justin")
print(module23.randict["name"])
print(module23.ranint1)

#2. alias of a module
import module23 as m23

a= m23.randict["age"]
print("\n2.\n", a)
x= dir(m23)
print(x)

#3. built-in modules
print("\n3.")
import platform
a=platform.system()
print(X)

#4. import only the part of the module
print("\n4.")
from module23 import randict
x= randict["location"]
print(x)

"""
1. python identifiers cannot start with a number. 
    SO YOU DONT NAME YOUR MODULE STARTING WITH NUMBERS.

    You can call all variables, methods, functions, and iterables in a module.

2. you can make an alias of a module by
        import module23 as m23

    the dir() function lists all variables and functions in a method.
        could be used on a platform module, too.

3. there are several built-in modules like "platform" in py.

4. you can import only a part of the module by the following statement.
        from m23 import randict

        WHEN IMPORTING A MODULE WITH "FROM" KEYWORD,  
        do not use a module name when referring to elements in the module.                                                                                                                                                                                                  
"""