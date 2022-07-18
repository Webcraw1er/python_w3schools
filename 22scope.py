"""
A variable is only available from inside the region it is created. 
THIS IS CALLED "SCOPE"

"""

#1. there is somrthing called a scope
print("\n1.")
def myfunc1():
    x=300
    def innerfunc():
        print("inner: ", x)
    innerfunc()
myfunc1()

#2. If the names are the same, the py treat them as two seperate different variables 
print("\n2")
x= 300
def myfunc2():
    x=200
    print(x)
myfunc2()
print(x)

#3. go global

y=500
def myfunc3():
    global x
    x= 1000
    global y
    y=100
    
print("y is : ", y)
myfunc3()
print("after the function y is now : ", y)
print("x is : ", x)

"""
you can use the global keyword in two different ways.
1. first, use it to declare a global variable inside a local function.
2. second, use it to change the global inside a local function.(however the statement must
    be executed, or "BE SEEN".)

"""
