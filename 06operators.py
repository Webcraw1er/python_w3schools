# 1. arithmetic operators
# +, -, *, /, % modulus, ** exponentiation, // floor division
print(19%7)         #remainders
print(3 ** 4)       #승
print(33/6)         #버림 나눗셈

# 2. assignment operators
# all listed below, { &=, |=, ^=, <<=, >>= } are all bit operators
print("\n2")
y=10
x= float(y)
print(x)
x+=3
print(x)
x-=3
print(x)
x*=5
print(x)
x/=5
print(x)
x%=4
print(x)
x **= 4.3
print(x)
x //=5
print(x)

#3. comparison operators
#       { ==, !=, >, <, <=, >= }

# 4. logical operators
#       { and, or, not }
print("\n4")
x=5
if x < 10 and x > 3:
    print("yes")
else:
    print("no")
if x > 10 or x < 3:
    print("yes")
else:
    print("no")
if not(x<10 and x>3):
    print("yes")
else: 
    print("no")

#5. identity operators
#       { is, is not }   ==, !=
print("\n5")
x= 5
y= 5
if x is y:
    print("yeah")
else: 
    print("nah")
if x is not y:
    print("yeah")
else: 
    print("nah")

#6. membership operators
# used to test if a sequence is presented in an obect
#      { in , not in }
print("\n6")
x= {"banana", "apple"}
if "banana" in x:
    print("yeah")
else:
    print("nah")
