import random as rd

def play_updown() :
    cnt = 0
    x = 0
    print('===== 2. 업다운게임 =====')
    print(f'자, 시작합니다. 총 10번의 기회까지 주어집니다. 준비하세요.')
    com_num = rd.randint(1, 100)
    while x in range(0, 10):
        while True :
            user_num = int(input('입력(1~100, 종료=0) : '))
            if user_num > 100 :
                print('100 이상의 숫자를 입력하였습니다. 100이하의 숫자를 입력해주세요.')
            elif user_num in range(1,101):
                break
            else :
                print('잘못된 입력입니다. 다시 입력해주세요.')

        if user_num == 0:
            print('게임을 종료합니다.')
            return
        elif user_num < com_num:
            x += 1
            print(f'[{x}]회 시도, 업!')
        elif user_num > com_num:
            x += 1
            print(f'[{x}]회 시도, 다운!')

        elif user_num == com_num:
            print(f'[{com_num}], 정답입니다~~')
            cnt += x
            break

    if cnt > 0 :
        print(f'총 10회 중 {cnt}회만에 정답을 맞추었습니다.')
    else :
        print(f'아쉽게도 10회 시도 중 맞추지 못해 실패하였습니다.\n'
              f'정답은 {com_num}입니다.')



