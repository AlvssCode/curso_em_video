# Exercício 9 – Tabuada
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
