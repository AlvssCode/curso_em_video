# Exercício 35 – Analisando Triângulo v1.0
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Informe o primeiro lado: '))
b = int(input('Informe o segundo lado: '))
c = int(input('Informe o terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('É um triângulo.')
else:
    print('Infelizmente não é um triângulo ')
