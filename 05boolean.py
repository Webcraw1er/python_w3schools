#1. simple booleans
from operator import truediv


print(10>9)
print(10==9)
print(10<9)

#2. bool() evaluates any value
print("\n2.")
print(bool("hello"))
print(bool(15)) #<--SINCE THESE both have values, they are considered true.
       
# 3. functions can return bool.
def myfunction():
    return True

x= myfunction()
print("\n3\n", x)
print(myfunction())
if myfunction():    # === if(myfunction()){
    print("yeah")
else:
    print("nay")

#4. check datatype
print("\n4")
x= True
print(isinstance(x, bool))



"""
1.  #an empty string, "0", and empty sets are considered False.
    { (), [], {}, "", 0, none, false }   are considered false.
    others are true.

2. When the bool is used as a value, the first letter must be upper cased.
    ex) true, false  (X)
        True, False  (O)


"""

