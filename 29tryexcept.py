"""
try     : lets you test a block for errors
except  : lets you handle the error(executed when there is an error.)
else    : lets you execute ethe code when theres no errors
finally : lets you execute the code regarless of the result of the try-exept blocks
            (regaRLESS of whether theres an error or not)


"""

#1. try excpet 
print("\n1.")
try:
    print(x)
except NameError:
    print("Variable x is not defined.")
except:
    print("Some exception occured.")

#2. try else
print("\n2.")
try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("printed successfully")

#3. finally
print("\n3.")
try:
    print(y)
except: 
    print("something clearlt went wromg")
finally:
    print("try else finished")

#4. example of try except
print("\n4.")
try:
    f= open("demofile.txt")
    try: 
        f.write("lorum lorum")
    except:
        print("something went wrong while writing to the file")
    finally:
        f.close()
except:
    print("something went wrong opening the file")

#5. raise
print("\n5.")
x= -1
if x< 0:
    #raise Exception("sorry, no numbers below zero")
    x=x
x= "helo"
if not type(x) is int:
    #raise TypeError("Only integers are allowed")
    x=x


"""
1. you can define as many exception blocks yuo want
        you can even define a special bloock of code for a special kind of error.

5. you can defien errors with "raise" keyword. 
    the error messages are Capoitalized remember that,
"""