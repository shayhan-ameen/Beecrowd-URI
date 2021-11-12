num = 0
total_age = 0
while True:
    age = int(input())
    if age<0:
        break
    total_age += age
    num +=1

print(f'{total_age/num:.2f}')