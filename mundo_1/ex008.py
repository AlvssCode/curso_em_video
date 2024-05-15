# Exercício Python 8 - Conversor de Medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite um valor em metros: "))

cm = metros * 100
mm = metros * 1000

print(f"{metros} metros é igual a {cm:.0f} centímetros e {mm:.0f} milímetros.")
