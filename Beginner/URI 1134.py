fuels = {1:0,
        2:0,
        3:0}
while True:
    type = int(input())
    if type==4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {fuels[1]}')
        print(f'Gasolina: {fuels[2]}')
        print(f'Diesel: {fuels[3]}')
        break
    elif type in fuels:
        fuels[type] +=1