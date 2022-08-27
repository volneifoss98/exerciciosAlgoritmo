
cigarroDia = int(input('Quanto cigarros voce fuma por dia? '))
anosFumando = int(input('A quantos anos voce fuma? '))

cigarroFumado = (cigarroDia * 365 ) * anosFumando
tempoPerdido = (cigarroFumado * 10)/1440

print(f"Voce ja perdeu {tempoPerdido} dias, pelo tempo fumado calculado")

