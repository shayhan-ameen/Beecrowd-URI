while True:
    x, y = list(map(int, input().split()))
    if x==y:
        break
    print('Decrescente') if x>y else print('Crescente')