"""
1. .format() method formats the result so the result is shown as expected.
    it formats the selected part of the string.

2. when the data is derived from a database ot a user input, they are not shown as expected.
    to control such values, we add placeholders( curly brackets{} ) in the text, and
    run the values through the format() method.

"""
#1. format
print("\n1.")
price= 49
txt = "the price is {} dollars."
print(txt.format(price))
txt= "the price is {:.2f} dollars"
print(txt.format(price))

#2. multi values and indexing
print("\n2.")
quantity= 3
itemno= 576
price= 41
myorder= "I want {} pieces of item number.{} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder= "I want {0} pieces of item number.{1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
myorder= "I want {0} pieces of it.{0} pieces for {2:.1f} dollars"
print(myorder.format(quantity, itemno, price)) 

#3. named indexes
myorder= "I have a {carname}, it is a {model}"
print(myorder.format(carname= "Ford", model= "Mustang"))





"""
1. you can change how the result is printed 
    ex) {:.2f}      : 소수점 두자리까지

3. when you use named indexes
    you must write things occordingly in the print() function.

"""