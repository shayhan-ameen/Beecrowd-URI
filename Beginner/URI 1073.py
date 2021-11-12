N = int(input())

N = N if N%2 == 0 else N+1

[print(f'{i}^2 = {i**2}') for i in range(2, N+1, 2)]