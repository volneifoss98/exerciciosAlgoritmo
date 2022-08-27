from __future__ import annotations


anoNascimento = int(input('Informe seu ano de nascimento '))
idade = 2022 - anoNascimento
idadeFuturo = idade - 18
idadePassado = 18 - idade

if idade > 18:
    print(f"Ja passou {idadeFuturo} ano(s) do seu alistamento")
else:
    print(f"faltam {idadePassado} ano(s) para seu alistamento")