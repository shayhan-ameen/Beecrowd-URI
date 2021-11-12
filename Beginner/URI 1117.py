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
        break
        
print(f'{num1=} and {num2=} media = {(num1+num2)/2:.2f}')