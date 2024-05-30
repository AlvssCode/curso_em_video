# Exercício 54 – Grupo da Maioridade
# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

maiores = 0
menores = 0
atual = datetime.now().year

for i in range(7):
    nascimento = int(input(f"Informe o ano de nascimento da pessoa {i+1}: "))
    idade = atual - nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Quantidade de pessoas que são maiores de idade: {maiores}")
print(f"Quantidade de pessoas que ainda não são maiores de idade: {menores}")
