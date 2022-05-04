"""
1. py is an object oriented lang.
    almost everything in py is an objects, with its properties and methods. 

2. A class is an object constructor, or a "blueprint" for creating objects.

"""

#1. creating a class
class MyClass:
    x= 5
print(MyClass)
print("You have made a \"MyClass\" class with property of 5") 
print("now you use the class \"MyClass\" to create objects")
p1=MyClass()
p1.x=10
print(p1.x)

#2. __init__()
print("\n2.")
class Person:
    def __init__(self, name1, age1):
        self.name=name1
        self.age=age1

p1=Person("John", 19)
print(p1.name)
print(p1.age)
#p2=Person()
#print(p2.name)


#3. Object Methods.
print("\n3.")
class Person:
    def __init__(self, personname, personage):
        self.name=personname
        self.age=personage
    def MyFunc(self):
        print("Hello my name is ", self.name, "\nand im ", self.age)
p1=Person("John", 19)
print(p1.name)
print(p1.age)
p1.MyFunc()

#4. self parameter(or arg)
print("\n4.")
class People:
    def __init__(mysillyobject, name, age):
        mysillyobject.name= name
        mysillyobject.age= age
    def myfunc2(yourself):
        print("my name is ", yourself.name)

p1=People("Justin", 26)
p1.myfunc2()

#5. modify, delete the object property or the obj itself
p1.age= 40
print("P1's age is: ", p1.age)
del p1.age
del p1

class Person:
    pass

"""
2. __init__() is a built-in fnction.
    All classes have an __init__() function, which is always executed when the class is initiated.
        STRICTLY SAYING, it is called automatically everytime the class is being used to create
        a new object.

    The user can define __init__() function to assign values to object properties, or other 
    operations that are necessary when an object is created.

    The user sort of snatches the __init__() to define the initiating values to assign 
    each objects' values easier.

        IF WE DO NOT DEFINE __INIT__()
            Try it yourself- in #1, if we write p1=MyCalss(10) instead of p1=MyClass() \n p1.x=10
            py raises an error that reads-> TypeError: MyClass() takes no arguments

            this is because you didn;t set the destination of the value, so it never takes an arg.
        
        ALSO iF WE DID DEFINE __INIT__() BUT DIDNT INITIATE THE OBJECTS WITH ARGUMENTS
            ex) if we did initialize the class, and write shit like p2=Person()
                -> then the py raises error that says
                Person.__init__() missing 2 required positional arguments: 'name' and 'age'
        
3. methods can be called inthe code using the object's properties.
    
    def __init__(self, personname, personage):
        self.name=personname
        self.age=personage
    --> in this shit, .name is called a property of the class, and the personname/personage
        are just arguments given. 
            so its kinda like creating a new variable called "name", but its a property of the 
            class, so its written as self.name or shit.

4. Self parameter is the referenece of the current instance of the class
    and is used to access variables that belongs to the class

    It does not has to be named "self", it can be of any name you like, 
    BUT must come as the first parameter of any function is the class.

    this "self" parameter is set as a positional argument. It is present even if you can't see it,
    If you call a MyFunc1 that id defined as 
        def MyFunc1(self)
            print(self.name)
    you must call as objectName.MyFunc().
    If you add a parameter, You get an error
        People.myfunc2() takes 1 positional argument but 2 were given 
"""