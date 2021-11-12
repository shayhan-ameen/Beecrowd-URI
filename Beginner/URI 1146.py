lim = int(input())

while lim!=0:
    numbs = ''
    for numb in range(1, lim+1):
        numbs += str(numb)+' '
    #numbs = ''.join(str(numb)+' ' for numb in range(1, lim+1))
    print(numbs[:-1])
    lim = int(input())
