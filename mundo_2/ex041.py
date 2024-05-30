# Exercício 41 – Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:

from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JÚNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'Categoria: {categoria}')
