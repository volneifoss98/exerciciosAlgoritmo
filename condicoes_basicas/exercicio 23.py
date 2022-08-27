distanciaViagem = int(input('Digite a distancia que deseja viajar em KM: '))
totalComDesc = distanciaViagem * 0.45
totalSemDesc = distanciaViagem * 0.50

if distanciaViagem <= 200:
    print(f"Para percorrer a distancia de {distanciaViagem}, o total é de R${totalSemDesc}")
else:
    print(f"Para percorrer a distancia de {distanciaViagem}, o total é de R${totalComDesc}")