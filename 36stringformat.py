"""
string format: 문자열 형식화

1. there are three ways you can format a string.
    1) % and 서식기호   : c 의 printf처럼, 문자형과 1대1 매치로 진행(완전히 같음.).
    2) f-string         : 직접 변수명을 넣어서 빠르게 진행.
    3) .format()        : 순서 섞어서 function 에 parameter pass 할 때처럼, 
                        {0} ~ {n} 까지를 매치시킨다.
"""
#1. %, 서식기호
friendnames=  ["Justin", "John", "Ernie"]
for name in friendnames:
    print("his name is %s" % name)
money= 1000
s= "give me %d won" % money
print("\n", s)

for name in friendnames:
    print("%s gave me %d won. thanks" % (name, money))

#2. f-string
print("\n2.")
i=0
for i in range(len(friendnames)):
    print(f"{friendnames[i]} gave me {money} won. thanks.")

#3. .format()
print("\n3.") 
i=0
for i in range(len(friendnames)):
    print("{0} gave me {1} won. thanks".format(friendnames[i], money))

#ex) 구구단 7단
print("\n구구단 7단")
left=7
right=1
for right in range(1, 10, 1):
    print("{0} X {1} = {2}".format(left, right, left*right))
    right+=1

"""
"""