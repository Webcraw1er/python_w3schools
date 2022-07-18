#10. sorting the list
thislist=['apple', 'cherry', 'banana', 'lemon', 'orange', 'craenberry']
thislist.sort()
print(thislist)

thislist=[1, 45, 10, 34, 5, 44]
thislist.sort()
print(thislist) 

thislist=['apple', 'cherry', 'banana', 'Lemon', 'orange', 'Craenberry']
thislist.sort()
print("sort method is case-sensitive by default")
print(thislist)

thislist=['apple', 'cherry', 'banana', 'Lemon', 'orange', 'Craenberry']
thislist.sort(key= str.lower)
print("but you can make it case insensitive")
print(thislist)

#11. reverse sorting.
print("\n11")
thislist=['apple', 'cherry', 'banana', 'lemon', 'orange', 'craenberry']
thislist.reverse
print(thislist)
thislist.sort(reverse = True)
print(thislist)

#12. list copying
list1=[1, 2, 3, 4, 5]
list2=list1
list2.append(6)
print("list2", list2)
print("list1", list1)
print("so instead, we use .copy() method.")
list3= list1.copy()
list3.append(7)
print(list1)
print(list3)

#!3. concatenating lists
print("\n13")
list1= [ "a", "b", "c" ] 
list2= [1, 2, 3]
list3= list1+list2
print(list3)

list3.clear()
print(list3)
list3=list1.copy()
for x in list2:
    list3.append(x)
print(list3)

list3.clear()
print(list3)
list3=list1.copy()
list3.extend(list2)
print(list3)
"""
11. .reverse(list)          : simply reverses the current list.
    .sort(reverse = True)   : arranges the list by reversing order.

12. just using "=" operater like 
    list1= list2
    makes the two lists correspondant. 
    like in c, they share the same #address.
    so, without making them interfere with one another, you use .copy()
"""