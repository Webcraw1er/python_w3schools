"""
python has two primitive loop commands: while loops and for loops



"""

#1. creating while loops
print("\n1.")
i=0
while i < 4:
    print(i)
    i+=1

#2. break
print("\n2.")
i=1
while i<10:
    print(i)
    if i > 5:
        break
    i+=1

#3. continue
print("\n3.")
i=0
while i<8:
    if 3< i and i< 6:
        i+=1
        continue
    print(i)
    i+=1

#4. else in while loop
print("\n4.")
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")





"""
2. break is used to instantly stop the iteration
3. continue is used to stop the current iteration and CONTINUE WITH THE NEXT.  
4. else in "while loop" executes only once; when the conditional statement is no longer true;
    hence the loop comes to the end.
"""