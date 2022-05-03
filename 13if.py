"""
in conditional(if else) statements, we are going to use 
the following logical conditions
    ==  : equal
    !=  : not equal
    <   : lesser than
    >
    <=
    >=


"""

#1. simple if
a= 33
b= 200
if a<=b:
    print("\n1.\n", "a is smaller than b")
elif a==b:
    print("equal")

a= 33
b= 32
if a<b:
    print("b is greater than a")
elif a == b: print("a and b are equal")
else: print("b is lesser than a")

#2.
#3.
print("\n3.")
x=63
if x>10:
    print("its bigger thqn 10")
    if x>20:
        print("its even bigger than 20")
    else:
        print("but not above 20")
else:
    print("its under 10")
        

"""
1. elif     :is used when you want to set another condition, 
            this comes with a condition right after.
  else      : is used to collect everything that were not caught by the previous conditions,
            thus does not require a condition

    2) like shown above, if the statement you want to execute has only one line,
        you put it on the same line, right next to the condition.

2. && in python     : and
    || in python    : or

3. nested if        : you write multiple if(s), beware of the indents. 



"""