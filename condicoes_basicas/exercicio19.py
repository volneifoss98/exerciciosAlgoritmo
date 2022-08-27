numero = int(input('Digite um numero e vejamos se é par ou impar '))
restoDivisao = numero % 2
if restoDivisao == 0:
    print(f"o {numero} é par")
else:
    print(f"o {numero} é impar")