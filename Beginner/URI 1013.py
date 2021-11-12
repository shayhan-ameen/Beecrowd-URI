a, b, c = list(map(int, input().split()))

maxab= (a+b+abs(a-b))/2
result= int((maxab + c + abs(maxab - c))/2)

print(f'{result} eh o maior')