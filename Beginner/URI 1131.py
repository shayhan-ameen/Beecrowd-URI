total_games = 0
inter_wins = 0
gremio_wins = 0
draws = 0

inter_goals, gremio_goals = list(map(int, input().split()))
total_games += 1
if inter_goals>gremio_goals: inter_wins +=1
elif inter_goals<gremio_goals: gremio_goals +=1
else: draws +=1
while True:
    print('Novo grenal (1-sim 2-nao)')
    response = int(input())
    if response == 1:
        inter_goals, gremio_goals = list(map(int, input().split()))
        total_games += 1
        if inter_goals>gremio_goals: inter_wins +=1
        elif inter_goals<gremio_goals: gremio_wins +=1
        else: draws +=1
    else:
        print(f'{total_games} grenais')
        print(f'Inter:{inter_wins}')
        print(f'Gremio:{gremio_wins}')
        print(f'Empates:{draws}')
        if inter_wins>gremio_wins: print('Inter venceu mais')
        elif gremio_wins>inter_wins: print('Gremio venceu mais')
        else: print('Não houve vencedor')
        break
        
        
