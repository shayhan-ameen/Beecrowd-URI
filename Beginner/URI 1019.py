n = int(input())

seconds = n % 60
n = int(n/60)
minutes = n % 60
n = int(n/ 60)
hours = n

print(f'{hours}:{minutes}:{seconds}')
