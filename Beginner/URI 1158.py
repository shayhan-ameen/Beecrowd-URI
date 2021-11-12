tc = int(input())

for _ in range(tc):
    x, y = list(map(int, input().split()))
    x +=1 if x%2==0 else False 
    print(sum(i for i in range(x,x+(y*2),2)))
    