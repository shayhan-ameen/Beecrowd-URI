def gcd(a, b):
    while(a%b != 0):
        temp=a%b
        a=b
        b=temp
    return b


tc = int(input())
while tc:
    N1, ignoreChar1, D1, operand, N2, ignoreChar2, D2 = input().split()
    N1, D1, N2, D2 = list(map(int, [N1, D1, N2, D2]))

    if operand == '+':
        n = (N1*D2 + N2*D1)
        d = (D1*D2)
    elif operand == '-':
        n = (N1 * D2 - N2 * D1)
        d = (D1 * D2)
    elif operand == '*':
        n = (N1 * N2)
        d = (D1 * D2)
    else:
        n = (N1 * D2)
        d = (N2 * D1)
        #eans(N1 * D2) / (N2 * D1)
    commonFactor = gcd(n,d)
    print(f'{n}/{d} = {int(n/commonFactor)}/{int(d/commonFactor)}')
    tc=tc-1
