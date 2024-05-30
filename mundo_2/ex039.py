# Exercício 39 – Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.")

if idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento.")
    alistamento = ano_atual + saldo
    print(f"Seu alistamento será em {alistamento}.")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos.")
    alistamento = ano_atual - saldo
    print(f"Seu alistamento foi em {alistamento}.")
else:
    print("Está na hora de se alistar")
