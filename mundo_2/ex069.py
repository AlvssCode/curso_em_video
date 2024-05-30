# Exercício 69 – Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

add_age = add_men = add_women = 0

while True:
    try:
        age = int(input("Digite a idade: "))
        sex = str(
            input("Digite o sexo (M para masculino, F para feminino): ")).strip().upper()
    except ValueError:
        print("Entrada inválida. Por favor, tente novamente.")
        continue

    if age >= 18:
        add_age += 1

    if sex == "M":
        add_men += 1
    elif sex == "F" and age < 20:
        add_women += 1

    choice = str(
        input("Deseja continuar? (S para sim, N para não): ")).strip().upper()
    if choice == "N":
        print(f"Total de pessoas com mais de 18 anos: {add_age}")
        print(f"Total de homens cadastrados: {add_men}")
        print(f"Total de mulheres com menos de 20 anos: {add_women}")
        break
