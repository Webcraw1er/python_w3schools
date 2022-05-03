"""
dictionaries
1. ordered, changeable, doesnt allow duplicates
2. presented in a key: value pairs, and can be referred to by using key names.
    and the keys works as an index.
3. cannot have two items of the same key. 
    does not really raise an error, but the latter overwrites the former.
"""

#1. creating a dict
thisdict= {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964,
    "year"  : 2004,
}
print(thisdict)
print("The brand of the product is : ", thisdict["brand"])
print("length is : ", len(thisdict))
print("type is : ", type(thisdict))

#2. accessing the item
x= thisdict["model"]
print(x)
y= thisdict.get("model")
print(y)

x= thisdict.keys()
print(x)
x= list(thisdict.keys())
print(x)
x= tuple(thisdict.keys())
print(x)
x= set(thisdict.keys())
print(x)

x= thisdict.values()
print("\n" , x)
x= list(thisdict.values())
print(x)
x= tuple(thisdict.values())
print(x)
x= set(thisdict.values())
print(x)

x= thisdict.items()
print("\n" , x)
x= list(thisdict.items())
print(x)
x= tuple(thisdict.items())
print(x)
x= set(thisdict.items())
print(x)

#3. check if an item or key is in the dict.
print("\n3.")
thisdict["horsepower"]= 193
x= list(thisdict.items())
print(x)
if "horsepower" in thisdict:
    print("yes. horsepower is one of the keys in thisdict")

#4. changing items
x= thisdict.items()
print("\n4.\noriginal         : ", x) 
thisdict["year"]= 1964
print("\naltered          : ", x)
thisdict.update({"year": 1965})
print("\naltered again    : ", x)

#5. adding items
print("\n5.")
print(thisdict)
thisdict["price"] = "$1mil"        #why square brackets? because keys in dict are treated as indexes.
print(thisdict)
thisdict.update({"maker": "bentz"})
print(thisdict)

#6. removing dict items
thisdict.pop("maker")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["model"]
print(thisdict)
thisdict.clear()
print(thisdict)



"""
2.x= list(thisdict.items())    : saves the current items as a list.
`                                 saved as value, never changes even if thisdict is altered.
   x= thisdict.items()          : saves the items in adress served for the variable "x".
                                alterations will also change the values of x.

3. the key can be searched via the string, but the value cannot be.

5. adding and changing items can both use .update() methods. 
    update() method needs to be written on iterable objects with key: value pairs.

6. .pop("key") method deletes the specified item with key.
    .popitem() method removes the last inserted item
    del thisdict["key"] removes the item with key name.
    del thisdict erases the whole dictionary.
"""