min = int(input())
max = int(input())
if min>max: min, max = max, min
nums = range(min+1, max,1)
[print(num) if num%5==2 or num%5==3 else False for num in nums]
