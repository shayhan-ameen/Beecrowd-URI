import math
x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

result = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

print(f'{result:.3f}')