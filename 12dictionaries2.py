thisdict= {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964,
}

#7. looping through dict.
print("\n7.")
for x in thisdict:
    print(x, ": ", thisdict[x])
for x,y in thisdict.items():
    print(x, ": ", y)

#8. copying dict
print("\n8.")
thatdict = dict(thisdict)
print(thatdict)
thesedict= thisdict.copy()
print(thesedict)

#9. nested dict
print("\n9.")
JohnsFamily= {
    "child1"    : {
        "name"  : "Emil",
        "birth" : 1999,
    },
    "child2"    : {
        "name"  : "Jamil",
        "birth" : 2002,
    },
    "child3"    : {
        "name"  : "Ken",
        "birth" : 2005,
    },
}
print(JohnsFamily)

child01= {
    "name"  : "Justin",
    "birth" : 1999,
}
child02= {
    "name"  : "Britney",
    "birth" : 1996,
}
WilliamsFamily={
    "child01" : child01,
    "child02" : child02
}    
print(WilliamsFamily)

"""
1.using the ordinary for loop only prints the keys.



"""