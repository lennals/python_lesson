N = int(input('введите число кустов: '))
bushes = list(range(1,N+1))
print(bushes)
berries = []
if len(bushes) <= 2 :
    berries.append(sum(bushes))
else : 
    for i in range(len(bushes)):
        berries.append(bushes[i-1] + bushes[i-2] + bushes[i])    
print(f'Максимальное число собранных ягод - {max(berries)}')
    
