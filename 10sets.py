"""
set is unordered, unchangeable, unindexed, doesnt allow dups
set is unchangeable, but you can remove and add new items.

"""

#1. creating a set
print("\n1.")
thisset= {"apple", "banana", "apple", "cherry"}
print("thisset              : ", thisset)
print("length of thisset    : ", len(thisset))
print("type of thisset      : ", type(thisset))

#2. access set items
print("\n2.")
for x in thisset:
    print(x)
print("banana" in thisset)      # -> True or False value
print("Banana" in thisset)      

#3. add set items
print("\n3.")
thisset.add("orange")
print(thisset)

thatset= {"mango", "pineapple", "papaya"}
thisset.update(thatset)
print(thisset)

theseset= {"watermelon", "starfruit"}
thoseset= thisset.union(theseset)
print(thoseset)

#4. removing an item in the set
print("\n4.")
print(thisset)
thisset.remove("apple")
print(thisset)
thisset.discard("orange")
print(thisset)
thisset.discard("raspberry")
x= thisset.pop()
print(x)
print(thisset)



#5. removing a set as a whole
print("\n5.")
thisset.clear()
print(thisset)
del thisset
# print(thisset)

#6. intersactions of sets
print("\n6.")
thisset= {"apple", "mango", "melon", "fashionfruit"}
thatset= {"apple", "mango", "starfruit", "strawberry"}
thisset.intersection_update(thatset)
print(thisset)
theseset= thisset.intersection(thatset)
print(theseset)


"""
2. ( "apple" in thisset ) is an expression, and returns true or false(boolean), case insensitive

3. concatenating... or rather adding another iterable to sets uses
    .update() method
    ofcourse starting from the sets, it can add any iterables to a set.
    ofcourse without orders, thus unindexed.

    update() method does not return anything, but union() method does.
    the .union() method returns the concatenated set.

4. both the .remove() and .discard() methods delete items from the set.
    if the item called by the remove() method doesnt exist, it raises error.
    if the item called by the .discard() method doesnt exist, it does not raise error.

    remember that the set has no orders, so you cannot specify which item to remove with .pop() method.
        you can still use the .pop() method, but it will delete random item.
        meanwhile, .pop() method returns the deleted item, so you can save it in a variable 
        then print it.

6.  .intersection_update() method        leaves only theintersections in the original set.
    .intersection() method               returns a new set.
    .symmetric_deifference_update()      keeps the items that are not intersectioned
    .symmetric_difference()              same with above, but returns a new set. 

"""
