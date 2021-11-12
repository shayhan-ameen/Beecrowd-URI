def coordinates(x,y):
    if x==0 and y==0:
        return 'Origem'
    elif x==0:
        return 'Eixo Y'
    elif y==0:
        return 'Eixo X'
    elif x>0 and y>0:
        return 'Q1'
    elif x<0 and y>0:
        return 'Q2'
    elif x<0 and y<0:
        return 'Q3'
    else:
        return 'Q4'

x, y = map(float, input().split())

print(coordinates(x,y))