# Exercício 55 – Maior e menor da sequência
# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0


for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))
    if i == 1 or peso > maior:
        maior = peso
    if i == 1 or peso < menor:
        menor = peso

print(f"O maior peso lido foi {maior}kg e o menor peso lido foi {menor}kg.")
