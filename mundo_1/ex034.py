# Exercício 34 – Aumentos múltiplos
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: R$ "))

if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo = salario + aumento

print(f"O valor do aumento é de R${aumento:.2f}. O novo salário é de R${novo:.2f}.")
