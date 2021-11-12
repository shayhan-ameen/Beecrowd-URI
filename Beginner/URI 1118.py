num1 = float(input())
num2 = float(input())
while 1: 
    if not(0<=num1<=10):
        num1 = float(input())
        print('nota invalida')
    elif not(0<=num2<=10):        
        num2 = float(input())
        print('nota invalida')
    else:
        print(f'media = {(num1+num2)/2:.2f}') 
        new_calculation = 0
        while 1:
            if new_calculation == 1 or new_calculation == 2:
                break
            print('novo calculo (1-sim 2-nao)')
            new_calculation = int(input())
        if new_calculation == 1:
            num1 = float(input())
            num2 = float(input())
        elif new_calculation == 2:
            break
        
