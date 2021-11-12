min = int(input())
max = int(input())

if min>max:
    min, max = max, min

min = min+1 if min%2==0 else min+2
max = max-1 if max%2==0 else max-2

print(sum([i for i in range(min, max+1, 2)]))
