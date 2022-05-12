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

print(f.read())
f.close()

f= open("demofile.txt", "r")
print(f.read(10))
f.close()

#2. readline
print("\n2.")
f= open("demofile.txt", "rt")
print(f.readline())
i=0
for x in f:
    if i == 2:
        break
    print(x)
    i+=1
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
    왜냐 이미 ㅊ파일은 끝났고 공백만 남아있기 떄문.

2. if you want to iterate the read() method to read lines
    in your file, 

    f= open("demofile.txt", "r")
    for x in f:
        print(x)

    if you want to specify how many lines you want to print,
    write like the above code.


"""