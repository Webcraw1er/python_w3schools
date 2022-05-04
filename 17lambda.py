"""
    syntax
        lambda arguments : expression
1. lambda is a small anonymous function
2. can take any number of arguments, but can only have one expression

"""

x = lambda a: a + 10
print(x(5))

x= lambda a, b : a* b
print(x(5,6))

x= lambda x, y, z: x+ y+ z
print(x(2, 3, 4))

print((lambda x, y: x*y)(5,6))
# in this case (lambda x, y: x*y) is x in above syntax.


#2. more lambda usages
print("\n2.")

def myfunc(n):
    return lambda a: a* n
mydoubler = myfunc(2)
mytripler= myfunc(3)
print(mydoubler(11))
print(mytripler(11))

"""
1. the basic structure of the lambda function is as foollows.
        (lambda x, y: x*y)(5, 6)
    but you can save the first parenthesis into a variable if needed,
    and you can even write it as a function like in #2.
2. match #2 with the fuctions above.
you will be able to find out that the underlying syntax remains the same.
    for example, in
        1. def myfunc(n):
        2.     return lambda a: a* n
        3. mydoubler = myfunc(2)
        4. print(mydoubler(11))
    line num 1, 2, 3 can be summarized to 
        mydoubler= lambda a: a* 2
    this is clearly a basic lambda function, so mydoubler(11) will work just fine, just like in 
    lambda function.    
"""
