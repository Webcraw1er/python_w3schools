#1. print
print("1\n", "hello," + "world")

#2. concatenate
x=5
y="hello"
print("2\n", "x: "+str(x))
print("y: "+y)

#3. redeclaration
z= 4
z= "z: random name"
print("3\n", z)

#4. type casting, printing types
a= str(4)   # "4"
b= int(5)   # 5
c= float(3) # 3.0
d= 4
e= "apple"
d= e
c= "banana"
print("4\n",a) 
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

#5. multiple variables
print("5\n")
x, y, z= "orange", "banana", "cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
d, e, f= fruits
print("\n"+d)
print(e)
print(f)

#6. output variables
g= "python"
h= "is"
i= "awesome"
print("6\n", g, h, i)
g= "python "    # <-- note that there are spaces at the end
h= "is "
i= "awesome"
print(g +h +i)

#7. print with commas
j=5
k="justin"
#print(j+k) <------not valid
print("7\n", j, k) #<-------valid

#8. global, local variables
print("8")
x= "awesome"
def myfunc():
    x= "great"
    print("Python is "+x)
myfunc()
print("Python is "+x)

#9. make the local variable global
x= "fun"
def myfunc2():
    global x   # <--- this lets you change the value of the global v
    global y    # <--- this lets you create a global v
    x= "awesome"
    y= "cool"
myfunc2()
print("9")
print("Python is ", x)
print("Python is "+ y)

#10. escape
print("you can escape letters with \"\\\", just like this \"")

# 1. In Python, indentation is crucial, 
#   { } 대신 인덴트가 사용됨.인덴트는 최소 공백 하나 이상이어야 함.
#   YOU must use the same amount of indents in the same block.
# 2. every comments must have a "#" per each line.
#   if its in the end of the line, then the py ignores the rest of the line.
# 3. variables can change types afterwards according to the code written
#
# 4. but can be casted as int(), str(), float() 
#   these casted variables can also be changed.

# 5. Variable names are case-sensitive.
#   means that they vary according to the upper/lower cases.

# 6. variable names cannot have "-", " ", or numbers as a starting letter.

# 7. every string has an auto crlf at the end.
"""
this is a multiline comment, but as long as it is not assigned to a 
variable, the python will read it then ignore it, 
so it can be one way to write a multiline comment.
"""

