
num = int(input())
result = '0 1 '
#fibonacci = [0, 1]
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
for i in range(2,num):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1]) 
    result += str(fibonacci[i])+' '

print(result[:-1])