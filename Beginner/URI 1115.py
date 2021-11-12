
cartasian = [['', ''],
            ['', 'quarto']]

while 1:
    x, y = list(map(int,input().split()))
    if x==0 or y==0:
        break
    elif x>0:
        if y>0:
            quardant='primeiro'
        else:
            quardant='quarto'
    else:
        if y>0:
            quardant='segundo'
        else:
            quardant='terceiro'
        
    print(quardant)
