code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

code1, units1, price1 = [int(code1), int(units1), float(price1)]
code2, units2, price2 = [int(code2), int(units2), float(price2)]
totalAmount = units1*price1 + units2*price2

print(f'VALOR A PAGAR: R$ {totalAmount:.2f}')