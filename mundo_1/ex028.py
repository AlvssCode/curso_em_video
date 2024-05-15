# Exercício 28 – Jogo da Adivinhação v.1.0
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice
from time import sleep

ran = choice(range(6))

print("--=--" * 15)
print("Vou pensar em um número entre 0 e 5 e você deverá tentar adivinhá-lo.")
print("--=--" * 15)
num = int(input("Em qual número você acha que eu pensei?: "))
print("Pensando...")
sleep(1)

if 0 <= num <= 5:
    print(f"Número digitado: {num}.")
    if num == ran:
        print("Parabéns, você venceu!")
    else:
        print(f" O número correto era {ran}. Tente novamente.")
else:
    print("o número está entre 0 e 5!")
