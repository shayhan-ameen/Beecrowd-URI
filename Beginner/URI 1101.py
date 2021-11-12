while True:
    min, max = list(map(int, input().split()))
    if min <=0 or max <= 0:
        break
    if min>max: 
        min, max = max, min
    sum = 0
    for i in range(min, max+1):
        print(f'{i}', end=' ')
        sum += i
    print(f'Sum={sum}')