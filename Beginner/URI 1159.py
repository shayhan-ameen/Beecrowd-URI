while True:
    x = int(input())
    if x==0:
        break
    x +=1 if x%2==1 else False
    print(sum([i for i in range(x,x+10,2)]))
