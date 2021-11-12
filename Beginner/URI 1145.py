line, lim = list(map(int, input().split()))

num =1
for _ in range(1, int(lim/line)+1, 1):
    temp = ''
    for j in range(num, num+line, 1):

        temp += str(j)+ ' '
    print(temp[:-1])
    num +=line