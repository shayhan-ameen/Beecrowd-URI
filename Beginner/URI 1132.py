min = int(input())
max = int(input())
if min>max: min, max = max, min
nums = range(min, max+1,1)
print(f'{sum(list(filter(lambda x: x%13!=0 , nums)))}')


