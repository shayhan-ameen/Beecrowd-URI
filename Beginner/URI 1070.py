num = int(input())

num = num +1 if num%2 == 0 else num
[print(i) for i in range(num, num+12, 2)]