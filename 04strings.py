#1. strings
from re import X


x= "hello"
print(x)
x= """hello
nice to meet you
at least i do
and you?"""
print(x)

#2. string length
x= "hello there."
print("The length of the sentence is: ", len(x))  # space and comma are also one charecter.

#3. check if a word or charecter is in string
x= "hello my name is justin"
print("justin" in x)  # ->ture(boolean)
if "justin" in x:
    print("yes, 'justin' is in the sentence")


#4. slicing strings
x= "hello! my name is Justin!"
print("\nin the sentence 'hello! my name is Justin!'")
print(x[18: 24])
print(x[:5])
print(x[18:])
print(x[-7: -1])

#5. modify strings
x= "Hello guys! NICE to meet you!"
print("\n" + x.upper())
print(x.lower())
print(x.replace("NICE", "GLAD"))
print(x.split("e"))

#6 concatanate string
a= "Hello"
b= "world!"
c= a+b
print(c)
print(a+ " "+ b)
c= a+ " " + b
print(c)

#7 format
"""
이전에 배운 바와 같이 string 과 int등 numeric variables 는 합칠 수 없다.
그러니 
age= 36
txt= "hi. my age is " +age      따위를 할 수 없는 것.
하지만 format 메소드로는 된다!
"""
age= 36
txt= "hi. my age is {}"
print(txt.format(age))

quantity= 24
itemno= 4
price= 49.95
myorder= "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#or
myorder= "I want to pay {2}dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
"""
1. strings can come in between either " " and ' '

2. String in Python is a string, just like any other languages.
    also, there is no "char" data tyoe in python, so a single character is 
    simply an array with a length of 1.


"""