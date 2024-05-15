# Exercício 13 – Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Solicita ao usuário o salário do funcionário

salario = float(input("Digite o seu salário atual: "))
aumento = (salario * 15 / 100)
novo = salario + aumento
print(f"O seu novo salário de funcionário com 15% de aumento é: {novo:.2f}")
