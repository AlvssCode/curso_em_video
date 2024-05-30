# Exercício 58 – Jogo da Adivinhação v2.0
#  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print("Vamos iniciar o jogo! Estou pensando em um número de 0 a 10.")
numero_secreto = randint(0, 10)
chute = None
tentativas = 0

while chute != numero_secreto:
    chute = int(input("Qual é o seu chute? "))
    tentativas += 1
    if chute < numero_secreto:
        if abs(chute - numero_secreto) > 2:
            print("Você está longe. Meu número é maior! Tente de novo.")
        else:
            print("Você está perto. Meu número é maior! Tente de novo.")
    elif chute > numero_secreto:
        if abs(chute - numero_secreto) > 2:
            print("Você está longe. Meu número é menor! Tente de novo.")
        else:
            print("Você está perto. Meu número é menor! Tente de novo.")

print(
    f"Parabéns! Você descobriu o número {numero_secreto} após {tentativas} tentativas.")
