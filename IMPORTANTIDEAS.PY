import matplotlib.pyplot as plt
import numpy as np
import random
import time

l= lambda a: print("\n------\n%d.\n-----\n" % a)

l(1)
start_time= time.time()

container= {}
for i in range(6):
    container[i]= [1, 2, 3, 4]
print(container, "\n\n\n")

container2= {}
for i in range(6):
    container2['arr%d' % i] = np.array([])
    for j in range(4):
        rand= random.randrange(1, 10)
        z= np.array([rand])
        container2['arr%d' % i]= np.append(container2['arr%d' % i], z, axis=0)

for i in range(6):
    print(container2['arr%d' % i], "\n")


"""
1. Unlike html, in which you can make variable names with format ${ }, python does not allow this.
    Thus, when you want to make several 'name' = 'value' pairs, make a dictionary.
    Cause Python allows string formatting; and you can make names with formatting.



"""