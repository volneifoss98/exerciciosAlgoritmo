velocidadeCarro = int(input('Qual velocidade voce passou no radar? '))
multa = (velocidadeCarro - 80) * 5

if velocidadeCarro > 80:
    print(f'Voce tomou uma multa no valor de R${multa}')
else:   
    print('Voce não tomou multa')
