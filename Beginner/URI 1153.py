from itertools import product


n = int(input())
prod=1
for i in range(2, n+1,1):
    prod*= i 
print(prod)