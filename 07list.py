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
        # the extend() method has no limits in the form, you may add other lists, sets, dictionaries, 
        # or tuples.
print("\n5")
thislist.append("orange")
print(thislist)

thatlist=["craenberry", "strawberry", "jam"]
thislist.extend(thatlist)
print(thislist)
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

"""




