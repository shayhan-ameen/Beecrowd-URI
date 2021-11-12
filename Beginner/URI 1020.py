age = int(input())

years = int(age/365)
age = age%365
months = int(age/30)
days = int(age%30)

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')