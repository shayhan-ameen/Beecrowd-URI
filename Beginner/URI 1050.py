number = int(input())

phone_dialing = {61:'Brasilia',
                71: 'Salvador',
                11: 'Sao Paulo',
                21: 'Rio de Janeiro',
                32: 'Juiz de Fora',
                19: 'Campinas',
                27: 'Vitoria',
                31: 'Belo Horizonte'}

if number in phone_dialing:
    print(phone_dialing[number])
else:
    print("DDD nao cadastrado")