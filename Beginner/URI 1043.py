x, y, z = list(map(float,input().split()))

if x+y>z and x+z>y and y+z>x:
    perimeter = x+y+z
    print(f'Perimetro = {perimeter:.1f}')
else:
    area = ((x+y)/2)*z
    print(f'Area = {area:.1f}')