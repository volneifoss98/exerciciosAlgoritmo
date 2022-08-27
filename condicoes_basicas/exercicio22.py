nome = input('Olá, digite seu nome: ')
genero = input(f"{nome}, qual seu genero [F]feminino [M]masculino: ")
valorCompra = int(input(f"{nome}, qual o total de suas compras? "))

descMasculino = valorCompra - (valorCompra * 0.05) 
descFeminino = valorCompra -(valorCompra * 0.15)
if genero == 'F':
    print(f"{nome}, parabéns pelo seu dia, voce recebeu um desconto de 15%, total da sua compra é R${descFeminino}")
else:
    print(f"{nome}, voce ganhou um desconto de 5%, total da sua compra é R${descMasculino}")