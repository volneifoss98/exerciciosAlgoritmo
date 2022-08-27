nome = input('Diga seu nome: ')
nota1 = float(input('Escreva sua primeira nota '))
nota2 = float(input('Escreva sua segunda nota '))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f"{nome}, sua media é: {media}, voce teve um bom aproveitamento")
else:
    print(f"{nome}, sua media é: {media}, voce precisa fazer recuperaçao")