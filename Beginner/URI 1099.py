def sum_of_odds(min,max):
    if min > max:
        min, max = max, min
    min = min+1 if min%2 == 0 else min+2
    max = max-1 if max%2 == 0 else max-2

    return sum([num for num in range(min, max+1, 2)])


for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    print(sum_of_odds(x,y))
