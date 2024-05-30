# : Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.


inicio = int(input("Informe o valor inicial: "))
passo = int(input("Informe o passo da Progressão Aritmética: "))

final = inicio + (10 - 1) * passo

for valor in range(inicio, final + passo, passo):
    print(valor, end=', ')
print("Concluído.")
