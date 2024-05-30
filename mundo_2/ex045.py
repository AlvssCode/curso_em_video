# Exercício 45 – GAME: Pedra Papel e Tesoura
# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

escolhas = ['pedra', 'papel', 'tesoura']
computador = random.choice(escolhas)

print("Escolha: pedra, papel ou tesoura: ")
jogador = input().lower()

print("Computador escolheu...")
time.sleep(1)
print(computador)

if jogador == computador:
    print("Empate!")
elif (jogador == 'pedra' and computador == 'tesoura') or \
     (jogador == 'papel' and computador == 'pedra') or \
     (jogador == 'tesoura' and computador == 'papel'):
    print("Você ganhou!")
else:
    print("Você perdeu!")
