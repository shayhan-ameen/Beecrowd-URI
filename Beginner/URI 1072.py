N = int(input())
X = []
for _ in range(N):
    X.append(int(input()))

in_rng = sum([1 if 10<= num <=20 else 0 for num in X])
print(f'{in_rng} in')
print(f'{N - in_rng} out')