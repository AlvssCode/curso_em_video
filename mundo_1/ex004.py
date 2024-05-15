# Exercício 4 – Dissecando uma Variável
# faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input('Digite algo: ')
print(f'Tipo primitivo é: {type(a)}')
print(f'É alfanúmerico? {a.isalnum()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É decimal? {a.isdecimal()}')
print(f'É um dígito? {a.isdigit()}')
print(f'É minúsculo? {a.islower()}')
print(f'É númerico? {a.isnumeric()}')
print(f'Há espaços? {a.isspace()}')
print(f'Está capitalizada? {a.istitle()}')
print(f'É maiúsculo? {a.isupper()}')
