import math
a, b, c = list(map(float,input().split()))

D = b*b - 4*a*c
if a== 0 or D < 0:
    print('Impossivel calcular')
else:
    r1 = (-b+math.sqrt(D))/(2*a)
    r2 = (-b-math.sqrt(D))/(2*a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')