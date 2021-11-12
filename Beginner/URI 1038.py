x, y = list(map(int, input().split()))

price = [4.0, 4.5, 5.0, 2.0, 1.5]
result = price[x-1]*y


print(f'Total: R$ {result:.2f}')