"""
if you inherit a class, it carries all the ___init__() functione and the methods
from the parent class.


"""
#0. create a "Person" class
print("\n0.")
class Person:
    def __init__(self, firstname, lastname):
        self.fname= firstname
        self.lname= lastname
    def printname(self):
        print("The name is : \"", self.fname, " ", self.lname, "\"", sep='')

p1 = Person("John", "Miller")
p1.printname()

#1. create a child class(only inheriting, without any properties or methods of its own.)
print("\n1.")
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
s1= Student("Mike", "Olsen")
s1.printname()

#2. adding __init__() to the child class 
print("\n2.")
class Teacher(Person):
    def __init__(self, tage, tcareer):
        self.age= tage
        self.career= tcareer
t1= Teacher(29, "Teacher")
print("The age and career is : \"", t1.age, " ", t1.career, "\"", sep='')

#3. super() function that makes the child inherit all the properties and methods from parent.
class pilot(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.gradyear= 2019
    
    def printyear(self):
        print("and the graduation year is: ", self.gradyear)

    def printname(self):
        print("Simply, the name is ", self.fname, self.lname)

pilot1= pilot("Justin", "Kim")
pilot1.printname()
pilot1.printyear()


"""
1. like this, if you define your parent's __init__() inside the child's __init__(),
    the child inherits the parent.
    in this case, all of the arguments in the child's and the parent's function definition
    must make a match. 
        ex)
            class Student(Person):
                def __init__(self, fname, lname):
                    Person.__init__(self, fisrtname, lastname)
        will raise an error, while
            class Student(Person):
                def __init__(self, fname, lname):
                    Person.__init__(self, fname, lname)
        won't

    (((OR)))
    you can just wrote 
        pass
    instead of those two lines describing __init__() to
    inherit everything and at the same time dont append anything of its(child's) own. 
2. The child's __init__() function overrides the inheitance of the parent's __init__() function.
    in other words, the child will no longer inherit the parent's __init__() function

3. super().__init__()
    inherits every methos and properties from the parent. 
    THERE IS NO NEED TO WRITE "SELF" IN THE SUPER(). FUNCTION.

    the differnece between this and the "pass" is that
    IF YOU USE "PASS" 
        you will not be able to append anything more to your child.
    IF YOU USE "SUPER().__INIT__()"
        you will be able to append more properties and methods to your child.
    IF YOU USE "PARENT.__INIT__()"
        you just inherit the __init__() function of the parent, will all those methods aside.

    To make it short, you don't really use "pass" because there's no point in using this 
    unless you just want to change the name of the class a child belongs to.


    ALSO IN SUPER().
    class pilot(Person):
        def __init__(self, fname, lname, year):
            super().__init__(fname, lname)
            self.gradyear= year
    
    will raise an error because the number of arguments of the child and the parent must match.
    the first args are 4, and the second is 3. doesn't match.
    SO, if you really want to add a few more properties in the child, you would pretty much want to 
    just build a new __init__() function rather than inheriting it via super().__ or parent.__

    HOWEVER you are free to add new methods to the child tho.
    IF YOU ADD A METHOD THAT HAS THE SAME NAME WITH THE PARENT,
        it overrides the parent's method.
    
    


"""