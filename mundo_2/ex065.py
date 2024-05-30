# Exercício 65 – Maior e Menor valores
#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e
#  qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

flag = False
counter = adder = highest = lowest = 0

while not flag:
    n = int(input("Digite um número inteiro: "))

    adder += n
    counter += 1
    mean = adder / counter

    if counter == 1:  # Se for o primeiro número, ele é o maior e o menor
        highest = lowest = n
    else:
        if n > highest:
            highest = n
        elif n < lowest:
            lowest = n

    cont = str(input("Quer continuar? [SIM / NÃO] ")).strip().upper()
    if cont == "NÃO":
        flag = True

print(f"Média: {mean:.1f}")
print(f"Maior: {highest} | Menor: {lowest}")
