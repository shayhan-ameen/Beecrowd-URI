n = list(map(float,input().split()))

weights = [2,3,4,1]
avg = 0
for i in range(4):
    avg += n[i]*weights[i]
avg = avg/10.0

print(f'Media: {avg:.1f}')
if avg>=7:
    print(f'Aluno aprovado.')
elif 5<=avg<=6.9:
    print(f'Aluno em exame.')
    newScore = float(input())
    print(f'Nota do exame: {newScore:.1f}')
    finalAvg = (avg+newScore)/2.0
    if finalAvg>=5:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {finalAvg:.1f}')
if avg<5:
    print(f'Aluno reprovado.')
