N = int(input())
for _ in range(N):
    weights = [2.0, 3.0, 5.0]
    nums = list(map(float, input().split()))
    print(f'{sum([w*num for w, num in zip(weights, nums)])/sum(weights):.1f}')