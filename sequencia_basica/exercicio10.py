alturaParede = float(input("Digite a altura de sua parede:"))
larguraParede = float(input("Digite a largura de sua parede:"))

totalArea = alturaParede * larguraParede
quantidadeTinta = totalArea / 2
 
print(f"Total area a ser pintada {totalArea}m2")
print(f"Será necessário a quantidade de {quantidadeTinta} L de tinta")