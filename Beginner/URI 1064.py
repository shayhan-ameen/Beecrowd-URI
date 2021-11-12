
numbers = []
for _ in range(6):
    numbers.append(float(input()))

count = 0
sum = 0.0

for number in numbers:
    if number >= 0:
        sum += number
        count += 1

print(f'{count} valores positivos')
print(f'{sum/count:.1f}')