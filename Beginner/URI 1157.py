n = int(input())

[print(i) if n%i==0 else False for i in range(1,int(n/2)+1)]