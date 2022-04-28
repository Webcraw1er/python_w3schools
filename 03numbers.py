"""
Three numeric types: int, float, complex

int in python has unlimited length.

"""
#1.numeric types
print("1. Numeric types>")
x= 1        #int
y= 1.5      #float
y2= -87.7e5
y3= 12e10
z= 1j       #complex (ax+b 처럼 imaginary numbers a와 b, 그리고 숫자들로 표현된
z1= 5j      #   방정식 같은 표현식. 여기서 j는 variable 이 아니다.
z2= -5j
z3= 3+ 5j

print(y2)
print(y3)
print(z1)
print(z2)
print(z3)

#2. conversion of numeric types
print("2. conversion of numeric typs>")
x= 1
y= 2.8
z= 5j

a= float(x)
b= complex(y)
c= int(y)

print(type(a))  # 당연하게도, 상수는 complex로 치환 가능. ex)2 -> 2+0j 같이.
print(type(b))  # 하지만 complex를 상수로 치환은 불가능.
print(type(c))  # int(float)은 내림.
print(a)        # float(int) 은 끝에 .0이 붙음. 
print(b)
print(c)


#3. random numbers
print("\n"+" 3. random numbers")
#Python does not have a random() function. 
import random
print("random: ", random.randrange(1, 10))

#4. type castin
x= int(1)
y= int(2.8)
z= int("3")
print(x)
print(y)
print(z)

x= float(1)
y=float("2.3")
z= float("3")
print(x)
print(y)
print(z)

x= str("s1")
y= str(2)
z= str(3.1)
print(x)
print(y)
print(z)
