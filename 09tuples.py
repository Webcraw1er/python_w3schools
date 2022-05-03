"""
<tuples>
1. tuples are used to store multiple items in one variable.
2. tuples are ordered and unchangeble, and allow duplicates.
    by unchangeble we say that once the tuple has been created, 
    its items cannot be changed, added, or removed.
3. written in round brackets.
4. items are indexed.





"""
#1. creation of tuples.
thistuple=("apple", "orange", "apple", "watermelon")
print(thistuple)
print(len(thistuple))

thistuple=("apple",)
print(type(thistuple))
thistuple=("apple")
print(type(thistuple))

thistuple=("apple", 1, 12, True, "cat", 133, False)
print(thistuple[2])
print(thistuple[2:4])
print(thistuple[-2])
print(thistuple[-4:-1])

#2. editing tuples
print("\n2.")
x= (1, 2, 3, 4, 5)
y= list(x)
y[3]=5
x= tuple(y)
print(x)

#3. adding items to tuples
print("\n3.") 
thistuple=(1,2 ,3, 4)
y= list(thistuple)
y.append(5)
thistuple=tuple(y)
print(thistuple)

thattuple=(6,)
thistuple+=thattuple
print(thistuple)

thattuple=(7, 8, 9)
thistuple+=thattuple
print(thistuple)

#4. deleting an item in a tuple
print("\n4.")
x= list(thistuple)
x.remove(9)
thistuple=tuple(x)
print(thistuple)

del thistuple
#print thistuple      <------this causes error because thistuple no longer exists.

#5. packing and unpacking
print("\n5.")
fruits= ("apple", "banana", "cherry")       #apple, banan, cherry are "values"
(green, yellow, red)= fruits                #green, yellow, red are "variables"
print(green)
print(yellow)
print(red)

numbers=(1,2, 3, 4, 5, 6, 7, 8, 9)
(first, second, *third)= numbers
print(first)
print(second)
print(third, "\n")
(first, *second, third)= numbers
print(first)
print(second)
print(third, "\n")

#6. looping tuples
print("\n6.")
numbers= ( 1, 2,3, 4)
for x in numbers:
    print(x)
i=0
for i in range(len(numbers)):
    print(numbers[i])
i=0
while i<len(numbers):
    print(numbers[i])
    i+=1

#7. join tuples
tuple1=(1, 2, 3)
tuple2= ("a", "b", "c")
tuple3= tuple1+tuple2
print(tuple3)

thistuple=(1, 2, 3, 4, 5)
thistuple*=2
print(thistuple)
thistuple=(1, 2, 3,4)
tuple4= thistuple*2
print(tuple4)

thistuple=("apple", "orange", "apple", "watermelon", "orange")
print(thistuple.index("orange"))    # -> returns only the first index
print(thistuple.count("orange"))    # -> returns the number of the value used in the tuple.



"""
2. you cannot alter the value of a tuple directly, 
    so you first convert it to a list and then change the value, and then 
    alter it back to tuple.

5. when we create a tuple, we addign values to it, which is called "packing".
    In python, we are allowed to extract the values back into variables, which is called "unpacking"

    if you have more values than variables, use the asterisks to assign miltiple values.
        they will be saved as a list.

7. if you want to concatanate two tuples you just "+" them.
    if you multiply a tuple, it repeats the contents bu the given number.
"""

