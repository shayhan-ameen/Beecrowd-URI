n = float(input())

notes = int(n)
coins = int((n-notes)*100)

print('NOTAS:')
print(f'{int(notes/100)} nota(s) de R$ 100.00')
notes=notes%100
print(f'{int(notes/50)} nota(s) de R$ 50.00')
notes = notes%50
print(f'{int(notes/20)} nota(s) de R$ 20.00')
notes = notes%20
print(f'{int(notes/10)} nota(s) de R$ 10.00')
notes = notes%10
print(f'{int(notes/5)} nota(s) de R$ 5.00')
notes = notes%5
print(f'{int(notes/2)} nota(s) de R$ 2.00')
notes = notes%2
coins = coins + notes*100
print('MOEDAS:')
print(f'{int(coins/100)} moeda(s) de R$ 1.00')
coins = coins%100
print(f'{int(coins/50)} moeda(s) de R$ 0.50')
coins = coins%50
print(f'{int(coins/25)} moeda(s) de R$ 0.25')
coins = coins%25
print(f'{int(coins/10)} moeda(s) de R$ 0.10')
coins = coins%10
print(f'{int(coins/5)} moeda(s) de R$ 0.05')
coins = coins%5
print(f'{coins} moeda(s) de R$ 0.01')