# Exercício 56 – Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

total_idade = 0
age_old_men = 0
old_men = ""
mulheres_menos_20 = 0

for i in range(2):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    total_idade += idade

    if sexo == "M" and idade > age_old_men:
        idade_homem_mais_velho = idade
        old_men = nome

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 2

print(f"A média de idade do grupo é de {media_idade} anos.")
print(f"O nome do homem mais velho é {old_men} e ele tem {age_old_men} anos")

if mulheres_menos_20 == 0:
    print("Nenhuma mulher tem menos de 20 anos.")
else:
    print(f"{mulheres_menos_20} mulheres têm menos de 20 anos.")
