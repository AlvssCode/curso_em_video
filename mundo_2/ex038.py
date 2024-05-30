# Exercício 38 – Comparando números
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior")
