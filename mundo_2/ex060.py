# Exercício 60 – Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número: "))
fatorial = 1
i = 1

while i <= numero:
    fatorial *= i
    i += 1

print(f"O fatorial de {numero} é {fatorial}")
