x = int(input())
z=int(input())
while z<=x:
    z = int(input())
count = 1
num = x
while num<=z:
    num += x+count
    count +=1
print(count)
