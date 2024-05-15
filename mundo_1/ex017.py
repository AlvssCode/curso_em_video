# Exercício 17 – Catetos e Hipotenusa
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# hypot() do módulo math calcula a hipotenusa de um triângulo retângulo dado os comprimentos dos catetos.
from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ce = float(input("Comprimento do cateto adjacente: "))

hipotenusa = hypot(co, ce)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}.")
