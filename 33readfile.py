"""
once you have opended the file, you should manipulate it.

1. The built-in open() function returns a file object,
    and has a .read() method for reading the content of the file.

    just stating f.read()  does not do anything.
    you should write
    print(f.read())

"""
#1. reading the file
try:
    f= open("demofile.txt", "rt")
except:
    print("There is no such file")
else: 
    print("file opened")

crlf= "\n"
print(f.read(), crlf)
f.close()

f= open("demofile.txt", "r")
print(f.read(10))
f.close()

#2. readline
print("\n2.1")
f= open("demofile.txt", "rt")
print("first line: ", f.readline())
i=0
for x in f:
    if i == 1:
        break
    print(x)
    i+=1
print(f.readline())    
f.close() 


print("\n2.2")
f= open("demofile.txt", "rt")
print("first line: ", f.readline())
i=0
for x in f:
    if i == 2:
        break
    print(x)
    i+=1
print(f.readline())    
f.close() # <- why this happens(how 2.1 and 2.2 is different)? explained below.
# you see, when a file is opened and read, the next read() or readline() method will continue
# on the next line of the "latest line that was most recently read".
# so in 2.1,    line1 was read by readline(),
#               line2 was read by "for in", index 0  
#               line3 was read by "for in", index 1
#               line4 WAS read by "for in", index 2, and then broke(it IS INDEED read, only not printed.)
#               And then the last readline() method read nothing(read spaces) because no more line was left to read

# now look at 2.2.
#               line1 was read by readline(),
#               line2 was read by "for in", index 0  
#               line3 WAS read by "for in", index 1, and then broke(it IS INDEED read, only not printed.)
#               line4 WAS READ by readline() finally.

#          Heres the differnece between 2.1 and 2.2
#               
"""
1. 파일 경로 설정 시
    1) 만약 파일이 같은 폴더 내에 있다:
        read(test.txt)
    2) 만약 상위 폴더에 잇다:
        read(../test.txt)
    3) 만약 D 디스크의  Python 폴더에 있다:
        read(D:/Python/test.txt)

    you can also specify how many characters you will read by
        f.read(num)

    ******한번 파일을 열고, 그 매개체인 f로 익기 시작하면, 
    그 다음 read 매서드는 무조건 그전에 끝난 지점부터 시작함.
    그러니 f.read()로 이미 다 읽어버렸는데
    또 f.read(5) 등으로 읽어버리면 그냥 공백만 나온다. 
    왜냐 이미 파일은 끝났고 공백만 남아있기 떄문.

2. if you want to iterate the read() method to read lines
    in your file, 

    f= open("demofile.txt", "r")
    for x in f:
        print(x)

    if you want to specify how many lines you want to print,
    write like the above code.


"""