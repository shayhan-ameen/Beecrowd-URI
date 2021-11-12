start, end = list(map(int, input().split()))

duration = end-start
if duration==0:
    print('O JOGO DUROU 24 HORA(S)')
else:
    if duration>0:
        print(f'O JOGO DUROU {duration} HORA(S)')
    else:
        print(f'O JOGO DUROU {24+duration} HORA(S)')
