#print
print("hello," + "world")

#concatenate
x=5
y="hello"
print("x: "+str(x))
print("y: "+y)

#redeclaration
z= 4
z= "z: random name"
print(z)

#type casting, printing types
a= str(4)   # "4"
b= int(5)   # 5
c= float(3) # 3.0
d= 4
e= "apple"
d= e
print(a) 
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

#multiple variables
x, y, z= "orange", "banana", "cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
d, e, f= fruits
print("\n"+d)
print(e)
print(f)

#output variables
g= "python"
h= "is"
i= "awesome"
print("\n"+g, h, i)
g= "python "    # <-- note that there are spaces at the end
h= "is "
i= "awesome"
print(g +h +i)

#print with commas
j=5
k="justin"
#print(j+k) <------not valid
print(j, k) #<-------valid

#global, local variables
x= "awesome"
def myfunc():
    x= "great"
    print("Python is "+x)
myfunc()
print("Python is "+x)

# make the local variable global


# 1. In Python, indentation is crucial, 
#   { } 대신 인덴트가 사용됨.인덴트는 최소 공백 하나 이상이어야 함.
#   YOU must use the same amount of indents in the same block.
# 2. every comments must have a "#" per each line.
#   if its in the end of the line, then the py ignores the rest of the line.
# 3. variables can change types afterwards according to the code written
#
# 4. but can be casted as int(), str(), float() 

# 5. Variable names are case-sensitive.
#   means that they vary according to the upper/lower cases.

# 6. variable names cannot have "-", " ", or numbers as a starting letter.

# 7. every string has an auto crlf at the end.
"""
this is a multiline comment, but as long as it is not assigned to a 
variable, the python will read it then ignore it, 
so it can be one way to write a multiline comment.
"""

