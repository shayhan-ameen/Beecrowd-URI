numbers = []

for _ in range(5):
    numbers.append(int(input()))


even = sum([1 if number%2 == 0 else 0 for number in numbers])
odd = sum([1 if number%2 == 1 else 0 for number in numbers])
pv = sum([1 if number>0 else 0 for number in numbers])
nv = sum([1 if number<0 else 0 for number in numbers])

print(f'{even} valor(es) par(es)')
print(f'{odd} valor(es) impar(es)')
print(f'{pv} valor(es) positivo(s)')
print(f'{nv} valor(es) negativo(s)')




