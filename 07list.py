#used to store multiple items in one variable
# 1. list defitition and characteristics    
#   definition is placed above, characteristics below
#   1. list items are ordered(as arrays), changeble, and allow duplicate values.
#   2. list items has indexes, starting from the first item as [0]th element
#   3. order cannot e changeed
#   4. stack structure(new items placed at the end of the list
print("1")
#thislist = ["apple", "banana", "apple", "cherry", 1, True, 5]
thislist = (("apple", "banana", "apple", "cherry", 1, True, 5))
print(thislist)
if "apple" in thislist:
    print("yeah")
print("the length of the list is: ", len(thislist))

#2. range of the list
print("\n2")
print(thislist[1])         # [0] is first and [1] is second,
print(thislist[-2])        # whereas [-1] is last and [-2] is second last
print(thislist[2:6])       # note that index [2] is included but [6] is not. only up to [6-1]
print(thislist[:4])        # same here, only present list up to index [3], as a result, 4 items.
print(thislist[-5:-2])     # present from "-5th element" which is "apple", up to "-3th element" (int)1

#3. changing list items
print("\n3")
thislist= ["apple", "banana", "cherry", "orange", "kiwi"]
thislist[1]= "blackcurrant"
print(thislist)

thislist[1:3]= ["watermelon", "mango"]      # index [1] to index[3-1]
print(thislist)

thislist[5:7]= ["lemon", "fashionfruit"]    # if the list you want to exchange exceeds
print(thislist[5:7])                         # the current list, python automatically lengthen the list
                                            # to contain those

#4. inserting an element in the list(specific position)
print("\n4")
thislist=["apple", "banana", "lemon"]
thislist.insert(1, "cherry")
print(thislist)

#5. append & extend into the last position of the list.
        # the extend() method has no limits in the object forms, you may add other lists, sets, dictionaries, 
        # or tuples.
print("\n5")
thislist.append("orange")
print(thislist)

thatlist=["craenberry", "strawberry", "jam"]
thislist.extend(thatlist)
print(thislist)

#6. removing the list
print("\n6.")
thislist.remove("lemon")
a= thislist.pop(2)
print(a)
thislist.pop()
print(thislist)
del thislist[1]
print(thislist)
thislist.clear()
print(thislist)
del thislist
# print(thislist)   <--- error! thislist doesnt exist!

#7. loop list
print("\n7.")
thislist= ['apple', 'cherry', 'banana', 'lemon', 'orange', 'craenberry', 'strawberry', 'jam']
print("\nfor loop:")
for x in thislist:
    print(x)
print("\nsecond for loop:")
for i in range(len(thislist)):
    print(thislist[i])
print("\nwhile loop:")
i=0
while i < len(thislist):
    print(thislist[i])
    i+=1

#8. list comprehension
print("\n8.")
newlist1= []
for x in thislist:
    if "e" in x:
        newlist1.append(x)
i=0
for i in range(len(newlist1)):
    print(newlist1[i])

print("\nthe above code can be simplified into this ->")
newlist=[x for x in thislist if "a" in x]
print(newlist)

#9. more list comprehensions:
print("\n9.")
newlist2= [ x.upper() for x in thislist ]
print(newlist2)

newlist= ['hello' for  x in thislist]
print(newlist)

newlist3= [x if x!= "banana" else "orange" for x in thislist]
print(newlist3)
# -> return the item if it is not banana, if it is then return it as orange.


"""
1. lists can contain varius data types at once.

2. there are four collection data types in python using arrays.
    1) list: ordered, changeable, allow dup
    2) tuple: 튜플, ordered, unchangeable, allow dup
    3) set: unordered, unchangeable(though removing and adding item is possible), no dup
    4) dictionary: ordered, changeable, no dup

3. if the number of the elements you want to revixe exxceeds the number of the current elements,
    python automatically adjusts the length of the array to contain everything.

    when given less, it will revise the list accordingly again, which in this case
    erasing the remaining rest of the list.

4. when inserting the elements, python will take care of everything.

5. when appending, you may giv eonly one argument, and it will be placed at the enfd

6. .remove("item")      : removes the specified item
    .pop(index)         : removes the specified index
    .pop()              : removes the last item just like pop in stack structure.
    del thislist[1]     : removes index[1] in thislist.
    del thislist        : deletes the whole thislist.
    .clear()            : empties the list, the list remains, but it has no contents.

        in this case, the "del" is the keyword, and .pop, .remove are the methods.

8. the syntax of list comprehension 
    -> newlist = [ expression for item in iterable if condition == True ]

below is th example -->

    newlist= []
    for x in thislist:
        if "e" in x:
            newlist1.append(x)
    
this can be written as:
    newlist= [ x for x in thislist if "a" in x]       

9. newlist2= [ x.upper() for x in thislist ]
    can be interpreted as this -> for every x in thislist, apply the method "x.upper()"
    so in #8, you can say -> for every x in thislist, choose x respectively.
                            which is, while going through the for loop, choose all x's respectively.




"""




