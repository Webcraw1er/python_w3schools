"""
0. iteraBLES: containers like (lists, tuples, sets, dicts)
                all these objects have a iter() method which is used to get an iterator.
   iteraTOR : obtained from the iterable containers.
1. an iterator is an object that contains a countable number of objects.
2. It should be iterated upon, meaning that you can traverse through all the values.
3. Technically in py, an iterator is an object which implements the iterator protocol, 
which consists of the method __iter__() and __next__()

"""

#1. return an iterator from a tuple, and print each value.
mytuple={"apple", "banana", "cherry"}
myit= iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
for x in mytuple:
    print(x)

#2. iterator in a str
print("\n2.")
mystr="banana"
myit=iter(mystr)
print(next(myit), end='')
print(next(myit), end='')
print(next(myit), end='')
print(next(myit), end='')
print(next(myit), end='')
print(next(myit))
i=0
for x in mystr:
    i+=1
    if i == len(mystr):
        print(x)
    else:
        print(x, end='')

#3. create an iterator on your own.
    #that returns numbers.
class mynumbers:
    def __iter__(self):
        self.a= 1
        return self
    def __next__(self):
        x=self.a
        self.a+= 1
        return x

myclass= mynumbers()
myiter= iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#4. stopiteration

class mynumbers:
    def __iter__(self):
        self.a= 1
        return self
    def __next__(self):
        if self.a < 5:
            x=self.a
            self.a+= 1
            return x
        else:
            raise StopIteration

myclass= mynumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)
    


"""
1. The for loop actually creates an iterator object and executes the next() method for each loop.

3. to create an object/class as an iterator you have to implement the methods __iter__() and 
    __next__() to your object.

    Like you have learned, all classes have init functions, __init__() works similar.
        BUT MUST ALWAYS return the iterator object itself.
    
    the __next__()method also allows you to do operations, 
        AND MUST return the next item in the sequence.



"""