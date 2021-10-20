def hello():
    print("안녕하세요")

hello()

def message():
    print("A")
    print("B")

message()
print("C")
message()

def say1(name):
    string = '안녕하세요? ' + name + '님'
    return string

def say2(name):
    string = '안녕하세요? ' + name + '님'
    print(string)

name = "홍길동"
say1(name)
say2(name)

#name = input('당신의 이름은?')
print(name)

name =  input('당신의 이름은? ')
age = int(input('당신의 나이는? '))

print('당신은 ' + name + str(age) + '살입니다.')
print('당신은', name, '이고', age, '살입니다.')
print('당신은 {}이고 {}살 입니다.'.format(name, age))

date = input('오늘 날짜  :') #2021/10/20
print('오늘 날짜는', date, '입니다.')
