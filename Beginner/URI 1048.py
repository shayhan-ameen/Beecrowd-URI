salary = float(input())

increment = [[400, 0.15], [800, 0.12], [1200, 0.10], [2000, 0.07]]

newSalary = -1
for i in increment:
    if salary<= i[0]:
        newSalary = salary + salary*i[1]
        percentage=i[1]
        break
if newSalary == -1:
    newSalary = salary + salary * 0.04
    percentage = 0.04

print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {newSalary-salary:.2f}')
print(f'Em percentual: {int(percentage*100)} %')