"""
1. unlike for loops in other languages, for loops in python is used for iterating over a sequence,
which are lists, tuples, dictionaries, sets, or strings.
2. so with the for loops we can execute a set of statements once for each items in a list, 
tuple, set, etc.


"""
#1. varius looping i iterables
print("\n1.\n\nlooping list: ")
thislist= [ "apple", "banana", "cherry", "melon"]
for x in thislist:
    print(x)

print("\nlooping string: ")
for x in "banana":
    print(x)

#2. breaking for loop
print("\n2.")
for x in thislist:
    print(x)
    if x == "banana":
        break

#3. continue in for loop
print("\n3.")
for x in thislist:
    if x == "banana":
        continue
    print(x)

#4. NOT going through arrays
print("\n4.")
for x in range(6):
    print(x)
else:
    print("finished!")
print("\n")
for x in range(2, 8, 2):
    print(x)

#5. nested loop
print("\n5.")
adj=["tasty", "fine", "classy"]
fruits=["apple", "banana", "melon"]
for x in adj:
    for y in fruits:
        print(x, y)
else:
    print("I eat those!")

"""
4. the range() function defaults to increment the sequence by 1, but you can change it by adding a 
    number in the end like this ---> range(2, 8, 2).
                                    this will print 2, 4, 6. (no 8 since the range output is...)

    else:
        in the end of the for loop executes that one block of code at the end of the loop.

2. if the code "break"s out of the loop, then it will not execute the else: statement.

"""