anoNascimento = int(input('Me diga em que ano voce nasceu: '))
idade = 2022 - anoNascimento

if idade >= 16:
    print(idade)
    print('Voce já pode votar!')
else:
    print(idade)
    print('Voce ainda nao tem idade para participar das eleiçoes deste ano!')