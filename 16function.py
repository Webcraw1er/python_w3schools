"""
1. the function is a block of code which only runs when its called.
2. You might want to pass data, or parameters into a function.
    def myfunc(freind):     <--- argument: specified after the function name
        print(friend)
    myfunc("Tom")           <--- parameter: the data you want to paass into a function
"""

#1. creating a function
print("\n1.")
def myfunc(fname, num):    
    print("friend", num, ": ", fname, " ", sep='')

    num+=1
    return num
x=1
x= myfunc("Tom", x)
x= myfunc("Len", x)
x= myfunc("Amy", x)

def myfunc1_1(thatdict):
    print("this is the last name of the kid: ", thatdict["lastName"])
thisdict={"name": "Tom", "lastName": "Kellish", "age": 20}
myfunc1_1(thisdict)

#2. arbitrary arguments
print("\n2,")
def myfunc2(*kids):
    print("the youngest child is: ", kids[2], sep='')
myfunc2("Emil", "Tobias", "Linus")

def myfunc3(children):
#def myfunc3(*children):
    print("the youngest child is: ", children[2], sep='')
thistuple= ("Erney", "Tally", "Len")
myfunc3(thistuple)

#3. keyword arguments
print("\n3.")
def myfunc4(child1, child3, child2):
    print("the youngest child is child3, who is: ", child3)
myfunc4(child1="Emil", child2="Brian", child3="Katy")

#4. arbitrary keyword arguments, **kwargs
print("\n4.")
def myfunc5(**kidinfo):
    print("the age of the kid is: ", kidinfo["age"], "\nthe last name of the kid is: ", kidinfo["lname"])
myfunc5(name= "James", lname="Stwert", age=19)

#5. defeult parameter value:
print("\n5.")
def myfunc6(nation = "Korea"):
    print("the country I like the most is: ", nation, sep='')
nation1="US"
myfunc6("Norway")
myfunc6(nation1)
myfunc6()
myfunc6("Japan")

#6. recursion
print("\n6.")
def recur(x):
    if x> 0:
        result= x + recur(x-1)
        print(result)
    else:
        result= 0
    return result
print("Recursion example results")
recur(6)

"""
2. arbitrary arguments are written with *.
    so it may look like this ->  def myfuc(*randomarg)
    it is used when you are not aware of how many parameters you will recieve, 
    and the python will automaticlaly save all those parameters as a tuple in randomarg.
    So inside the function, you will access the data as items in tuples.

    if you directly pass a defined list, you will never use an *arg(arbitrary argument)
    because it is already an iterated object. So you must write the argument as 
    def myfunc(randomlist): , note that there is no star in front of the argument.

3. keyward arguments: lets you neglect the order of the arguments as written, by specifying
                      which value is stored for each key.

4. like *arg, you use this when you don't know how many parameters you will receive.
    if you write and call the function like this: ->

    myfunc5(**kidinfo): 
    myfunc5(name= "James", lname="Stwert", age=19)
    
    the parameters you passed will be saved in a dictionary like this.
    kidinfo={"name": "James", "lname": "Stwert", "age": 19}

6. you can write both 
    if (k< 0):
    if k< 0:
   ofcourse the former is easier to read, its uo to you.
"""
