#numbers = list(map(float,input().split()))
#print(numbers)
numbers = []

for _ in range(6):
    numbers.append(float(input()))

count = 0

for num in numbers:
    if num>=0:
        count = count + 1

print(f'{count} valores positivos')