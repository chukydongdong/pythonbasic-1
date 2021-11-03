#data = input("입력값: ")
data = 1
if int(data) % 2 == 0:
    print("짝수")
else:
    print("홀수")

hit = 0
while hit < 10:
    hit = hit +1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit ==10:
        print("나무가 넘어갔습니다.")
    elif hit ==8:
        print("나무가 곳 넘어갈 것 같습니다. ")
    elif hit ==1:
        print("나무를 10번정도 찍어야 넘어갈 것 같습니다. ")

prompt = """
100을 입력하면 종료가 되는 프로그램입니다.
100.종료
Enter number: """
number = 0
while number != 100:
    print(prompt)
    number = int(input())

number = 0
while number < 10:
    number=number+1
    print(number)

number = 1
while number  <= 10:
    print (number)
    number = number + 1

print("숫자 두 개를 작은수부터 입력해주세요.")
min = int(input())
max = int(input())
while min <= max:
    print(min)
    min = min+1

for number in range(1,21,1):
    print(number)


for number in range(10,101,1):
    print(number)
단= int(input('구구단을 출력합니다. 몇 단인지 입력해주세요'))
for number in range(1, 10):
    string = '{}x{}={}'.format(단, number, 단 * number)
    print(string)

