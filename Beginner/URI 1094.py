animals = [[],[],[]]
for _ in range(int(input())):
    num,animal_type = list(input().split())
    num = int(num)
    if animal_type == 'C':
        animals[0].append(num)
    elif animal_type =='R':
        animals[1].append(num)
    else:
        animals[2].append(num)

rabbit = sum(animals[0])
rat = sum(animals[1])
frog = sum(animals[2])
total = rabbit + rat + frog

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbit}')
print(f'Total de ratos: {rat}')
print(f'Total de sapos: {frog}')
print(f'Percentual de coelhos: {(rabbit*100.0)/total:.2f} %')
print(f'Percentual de ratos: {(rat*100.0)/total:.2f} %')
print(f'Percentual de sapos: {(frog*100.0)/total:.2f} %')