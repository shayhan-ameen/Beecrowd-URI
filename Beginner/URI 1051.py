salary = float(input())

if 0<= salary <= 2000:
    tex = -1
elif salary <= 3000:
    tex = (salary-2000) * 0.08
elif salary <= 4500:
    tex = (1000 * 0.08) + ((salary - 3000) * 0.18)
else:
    tex = (1000 * 0.08) + (1500 * 0.18) + ((salary - 4500) * 0.28)

print('Isento') if tex == -1 else print(f'R$ {tex:.2f}')