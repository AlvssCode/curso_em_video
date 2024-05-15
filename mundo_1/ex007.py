# Exercício Python 7 - Média Aritmética
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

media = (num1 + num2) / 2

print(f"A média do aluno é: {media:.1f}")
