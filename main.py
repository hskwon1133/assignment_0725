import game.rps as rps
import game.updown as ud
import game.lottery as lt
while True :
    # 메뉴 출력
    print('===== 미니게임 =====')
    print('1. 가위바위보')
    print('2. 업다운게임')
    print('3. 로또 번호 맞추기')
    print('0. 종료')

    # 선택 입력받기
    menu = int(input('메뉴 번호를 입력해주세요 : '))
    #게임플레이
    if menu == 0:
        break
    elif menu == 1:
        rps.play_rps()
    elif menu == 2:
        ud.play_updown()
    elif menu == 3:
        lt.play_lottery()
    else :
        print('잘못된 정보를 입력하셨습니다. 다시 시도해주세요.')





