# Exercício 25 – Procurando uma string dentro de outra
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input("Digite o nome de uma pessoa: ")

yes = 'SILVA' in nome.upper()

print(f"O nome tem SILVA ? {yes}")
