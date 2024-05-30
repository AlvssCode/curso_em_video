# Exercício Python 53:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite a frase: ').replace(' ', '')).upper()

if frase == frase[::-1]:
    print(f'É um Palíndromo:{frase}Depois:{frase[::-1]}')
else:
    print('Não é um Palíndromo')
