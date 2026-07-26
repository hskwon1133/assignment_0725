import random as rd

def play_rps() :
    lst = ['가위', '바위', '보']
    cnt = 0
    x = 0
    print('===== 1. 가위바위보 =====')
    print(f'자, 시작합니다. 이기면 기회는 3회까지 주어집니다. 준비하세요.')
    while x in range(0, 3):
        x+=1
        com_rps = rd.choice(lst)
        print(f'{x}. 가위, 바위, 보!')
        while True :
            user_rps = input('입력(종료=0) : ')
            if user_rps in ['가위', '바위', '보', '0'] :
                break
            else :
                print('잘못된 입력입니다. 다시 입력해주세요.')
        if user_rps == '0':
            print('게임을 종료합니다.')
        #    return 0
        elif ((user_rps == "가위" and com_rps == '바위') or
              (user_rps == "바위" and com_rps == '보') or
              (user_rps == "보" and com_rps == '가위')):
            print(f'com: [{com_rps}], 이겼다!')
            cnt = cnt + 1
        elif ((user_rps == "가위" and com_rps == '보') or
              (user_rps == "바위" and com_rps == '가위') or
              (user_rps == "보" and com_rps == '바위')):
            print(f'com: [{com_rps}], 졌다...')
        elif user_rps == com_rps:
            print(f'com: [{com_rps}], 비겼다.')
    print(f'총 3회 중 {cnt} 이겼습니다.')
