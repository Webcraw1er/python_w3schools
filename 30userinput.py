"""
1. Python 2.7 uses raw_input() method,. while 
    3.6 uses input()

2. py stops executing when it comes to "input()", and continues when the user has 
    given some input.

3. every inputs are regarded as strings.
    so if you compare an input value with an integer, it raises an error.
"""

username= input("Enter Username: ")
print("Username is: ", username)