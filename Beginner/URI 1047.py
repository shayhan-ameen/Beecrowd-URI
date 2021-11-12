startH, startM, endH, endM = list(map(int, input().split()))

if startH==endH and startM==endM:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    minuteDif = endM - startM
    hourDif = endH - startH
    if hourDif<0:
        hourDif= 24+hourDif
    if minuteDif<0:
        minuteDif = 60+minuteDif
        if hourDif==0:
            hourDif= 23
        else:
            hourDif = hourDif - 1
    print(f'O JOGO DUROU {hourDif} HORA(S) E {minuteDif} MINUTO(S)')
