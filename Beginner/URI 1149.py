inputs = list(map(int, input().split()))
a, n = inputs[0], inputs[-1]
print(sum([a+i for i in range(n)]))