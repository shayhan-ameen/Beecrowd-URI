spentTime = int(input())
avgSpeed = int(input())

totalDistance = spentTime * avgSpeed
fuel = totalDistance/12

print(f'{fuel:.3f}')
