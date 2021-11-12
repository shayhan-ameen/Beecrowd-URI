numbers = list(map(int,input().split()))

original = tuple(numbers)
numbers.sort()
for i in numbers:
    print(i)
print()
for j in original:
    print(j)