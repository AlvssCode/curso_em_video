# Exercício 68 – Jogo do Par ou Ímpar
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

wins = 0

while True:
    player = int(input("Escolha um número entre 0 e 10: "))
    if player < 0 or player > 10:
        print("Por favor, digite um número inteiro entre 0 e 10.")
    else:
        computer = randint(0, 10)
        choice = str(input("Ímpar ou par? [I / P] ")).strip().upper()
        while choice not in ["P", "I"]:
            print("Por favor, escolha 'I' para ímpar ou 'P' para par.")
            choice = str(input("Ímpar ou par? [I / P] ")).strip().upper()

        print(f"Você escolheu: {'PAR' if choice == 'P' else 'ÍMPAR'}!")
        soma = player + computer
        print(f"O computador escolheu {computer}.")

        if (soma % 2 == 0 and choice == "P") or (soma % 2 != 0 and choice == "I"):
            wins += 1
            print(f"{soma} é {'par' if soma % 2 == 0 else 'ímpar'}, então você ganhou!")
        else:
            print(f"{soma} é {'par' if soma % 2 == 0 else 'ímpar'}, então você perdeu.")
            print(f"Vitórias consecutivas: {wins}")
            break
