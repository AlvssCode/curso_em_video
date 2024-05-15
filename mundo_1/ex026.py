# Exercício 26 – Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").upper()

contagem = frase.count('A')

primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1
