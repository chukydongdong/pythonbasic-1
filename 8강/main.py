for number in range(1, 21, 1):
    print(number)

for number in range(20, 31, 1):
    print(number)  

print("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
for number in range(min, max+1, 1):
    print(number)


print("출력할 단을 입력해주세요.")
단 = int(input())
for number in range(1, 10):
    string = '{}x{}={}'.format(단, number, 단 * number)
    print(string)

for 단 in range(2, 10):
    print("{}단 시작".format(단))
    for number in range(1, 10):
        string = '{}x{}={}'.format(단, number, 단 * number)
        print(string)
    print("{}단 끝".format(단))

a= 0
while a <10:
    a =a + 1
    if a % 2 == 0:
        continue
    print(a)

a = 0
while a < 10:
    a = a + 1
    if a == 5:
        print('{}입니다.'.format(a))
        break
    print(a)

for number in range(1, 1001, 1):
    if number % 3 == 0:
        print(number)











