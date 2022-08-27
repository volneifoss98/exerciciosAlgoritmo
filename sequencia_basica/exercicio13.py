kmRodado = float(input('Quantos km voce rodou com o carro? '))
diasAlugado = int(input('Quantos dias voce ficou com o carro? '))

precoTotalKm = kmRodado * 0.20
precoTotalDiasAlugado = diasAlugado * 90

total = precoTotalKm + precoTotalDiasAlugado
print(f"O custo do serviço prestado a voce ficou no total de R${total}")
