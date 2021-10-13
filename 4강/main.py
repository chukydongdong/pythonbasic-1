
print(hello[7])
print(hello[5])
hello="\"안녕.\" 철수가 인사를 했다."
print(hello[10])
hello="안녕하세요!"
print(hello[5])
print(hello[-1])
a="Life is too short, you need python"
print(a[-6])
# L, y, n
print(a[0])
print(a[-34])
a="Life is too short, you need python"
print(a[1:30])
number= "24가 2210"
print(number[-4:])
a=3
b=4
print(a+b)
a= "3"
b= "4"
print(a+b)
s1="좋은 아침 입니다!"
s2=s1[0:5] + s1[-1]
print(s2)
s1="python"
s2="java"
s3= s1+ ' ' +s2+ ' '
print(s3 * 4)
number=3
destination="힉교"
print("나는 사과 %d개를 먹었다. 그리고 %s에 갔다." % (number, destination))

def add(a,b):
    return a+b

e=3
f=4
a=add(e,f) # a = e,d = f
print(a)
add(10, 15)
print(add(10, 15))
add(100,120)
print(add(100,120))

#minus, a-b
def minus(a,b):
    return a-b
minus(120,100)
print(minus(120,100))

def multi(a,b):
    return a*b
multi(2,8)
print(multi(2,8))

def divi(a,b):
    return a/b
divi(3,3)
print(divi(3,3))
