"""
    SO WHAT THE HECK IS __name__?

1. HOW DOES PY WORK?
    in c, java, c++, etc.. you have a main() function that executes codes.
    HOWEVER IN PY, there is no main function; it only determines the precedance
    by indentations.

2. SO WHAT IS __name__???
    1) __name__ is a built-in variable.
    2) contains the name of the current module. 
            -> if it is directly executed, 
                                __name__ == "__main__"
            -> if not directly executed and been imported, 
                                __name__ == "module_name""

    ex)
            you write the below block of code in module.py
                def hello():
                    print("hello!")
                print(__name__)

            then you write below block of code in main.py
                import module
                print(__name__)
                module.hello()

            the result will be like this: 
                module
                __main__
                hello!

    SO you can pretty much figure out that when executed in the currently running code, 
        __name__ == "__main__" returns true.
    likewise in a module named "module3", __name__ == "__main__" returns false because 
    in module3, __name__ == "module3". 






"""