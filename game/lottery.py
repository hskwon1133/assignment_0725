'''
lottery win structure
1등 6개 번호 일치
2등 5개 번호 일치 + 보너스 번호 일치
3등 5개 번호 일치
4등 4개 번호 일치
5등 3개 번호 일치
'''
import random as rd


def play_lottery() :
    num_lst = list(range(1,46))
    x = 0
    cnt = 1
    print('===== 3. 로또 번호 맞추기 =====')
    print(f'1~45까지 숫자 중 내가 선택한 6개 숫자와 추첨으로 결정된 숫자가 일치하는 개수에 따라 당첨!')
    # 6자리 숫자 랜덤 결정하기
    com_num_lst = rd.sample(num_lst, 6)
    # 추가 보너스 숫자 랜덤 결정하기
    num_lst = [bonus_num for bonus_num in num_lst if num_lst != com_num_lst]
    bonus_num = rd.sample(num_lst, 1)
    # 6자리 번호 입력하기 (이렇게 하면 개발은 쉽지만 유저의 입력 오류가 많을 가능성 높음)
    # user_num = list(map(int, input('숫자 6개 입력(공백필수)').split()))
    user_num_lst = {}
    while x in range(0,6):
        x += 1
        while True:
            user_num = int(input(f'{cnt}번째 숫자 입력(1~45, 0=게임종료): ' ))
            if user_num > 45 :
                print('45 이상의 숫자를 입력하였습니다. 다시 입력해주세요.')
            elif user_num == user_num_lst :

                print('숫자를 중복 입력하였습니다. 다시 입력해주세요.')
            else :
                cnt += 1
                break

        if user_num == 0 :
            print('게임을 종료합니다.')
            return 0
        else :
            user_num_lst.append(user_num)


play_lottery()
