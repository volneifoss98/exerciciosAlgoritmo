ano = int(input('Digite o ano para saber se e bissexto ou nao: '))

if ano % 100 != 0 and ano % 4 == 0 or ano %400 == 0:
    print(f"O {ano} é bissexto")
else:
    print(f"O {ano} nao e bissexto")