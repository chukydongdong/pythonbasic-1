if 3<5:
    print("조건식이 true이므로 실행됩니다.")
if 3>5:
    print("조건식이 Faise이므로 실행되지 않습니다.")

#apple = 3
#if apple >= 5:
#    print("사과를 나누어 먹는다.")
#else:
#    print("사과를 혼자 먹는다.")

money = 10000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어 가라")

#rank = input('몇 등인가요(1또는 2)?')
rank = '1'
if rank == '1': # 조건: 등수가 1일때
    print('TV를 보며 편안하게 쉬세요. ')
else:
    print('설거지 당첨!')

#grade = int(input("몇 학년 인가요(1~6)?"))
#if grade >=2 and grade<=4:
    print("햄버거를 주세요")
#else:
 #   print("김밥을 주세요")

pizza = input('피자 가게가 열렸나요(예/아니요)?')
chickn = input('치킨 가게가 열렸나요(예/아니요)?')
중국집 = input('중국집이 열렸나요(예/아니요)?')
if pizza == '예':
    print('피자 가게로 가자')
elif chickn == '예':
    print('치킨 가게로 가자')
elif 중국집 == '예' :
    print('중국집으로 가자')
else:
    print('편의점에서 라면을 먹자')




