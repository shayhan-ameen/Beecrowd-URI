sum = 1.0
power=1
for i in range(3, 39+1, 2):
    sum += float(i/(2**power))
    power +=1
print(f'{sum:.2f}')

# sum = 1.0
# for power, i in enumerate(range(3, 39+1, 2), start=1):
#     sum += float(i/(2**power))
# print(f'{sum:.2f}')


