n = int(input())

numbs = [1,2,3];
for _ in range(n):
    print(f'{numbs[0]} {numbs[1]} {numbs[2]} PUM')
    numbs = [num+4 for num in numbs]