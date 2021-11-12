i = 0.0
while i<1.9:
    j = 1.0
    while j<=3.0:
        if i==int(i) and (i+j)==int(i+j):
           print(f'I={int(i)} J={int(i+j)}') 
        elif i==int(i):
            print(f'I={int(i)} J={(i+j):.1f}')
        elif (i+j)==int(i+j):
            print(f'I={i:.1f} J={int(i+j)}')
        else:
            print(f'I={i:.1f} J={(i+j):.1f}')
        j += 1.0
    i += 0.2
print(f'I=2 J=3')
print(f'I=2 J=4')
print(f'I=2 J=5')
