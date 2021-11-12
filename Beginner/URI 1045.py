numbers = list(map(float, input().split()))

numbers.sort(reverse=True)
A=numbers[0]
B=numbers[1]
C=numbers[2]
if A >= B + C: print('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2: print('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2: print('TRIANGULO OBTUSANGULO')
elif A**2 < B**2 + C**2: print('TRIANGULO ACUTANGULO')
if A==B==C: print('TRIANGULO EQUILATERO')
elif A==B or B==C or C==A: print('TRIANGULO ISOSCELES')