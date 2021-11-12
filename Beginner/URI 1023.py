#time limit exceeded
n = int(input())
cidade = 1
while n!=0:
    sample = []
    totalResident = 0
    totalConsumption = 0
    for i in range(n):
        resident, consumption = list(map(int, input().split()))
        meanConsumption = int(consumption/resident)
        totalResident += resident
        totalConsumption += consumption
        sample.append([resident, meanConsumption])
    sample.sort(key=lambda x:x[1])
    meanConsumption = sample[0][1]
    resident = 0
    sampleAggregated = []
    consumptionString = ""
    flag=0
    for i in range(n):
        if meanConsumption == sample[i][1]:
            resident += sample[i][0]
        else:
            sampleAggregated.append([resident, meanConsumption])
            if flag==0:
                consumptionString += str(resident) + "-" + str(meanConsumption)
                flag = 1
            else:
                consumptionString += " " + str(resident) + "-" + str(meanConsumption)
            resident = sample[i][0]
            meanConsumption = sample[i][1]
    sampleAggregated.append([resident, meanConsumption])
    if flag == 0:
        consumptionString += str(resident) + "-" + str(meanConsumption)
        flag = 1
    else:
        consumptionString += " " + str(resident) + "-" + str(meanConsumption)
    if cidade!=1:
        print()
    print(f'Cidade# {cidade}:')
    cidade +=1
    print(consumptionString)
    value = int(float("%.2f" % float((totalConsumption * 100) / (totalResident))));
    print(f'Consumo medio: {value/100:.2f} m3.')
    n = int(input())